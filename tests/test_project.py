"""Pytest suite for Temperature Argmax Monotonicity Criterion.

All tests use Monte Carlo on synthetic logits with known gap Delta.
"""

import numpy as np
import pytest

from empirical.verify import (
    check_corollary_1,
    check_corollary_2,
    check_corollary_3,
    check_theorem_1,
    check_theorem_2,
    prediction_conservative_threshold,
    tempered_softmax,
    threshold_temperature,
    top1_probability,
)


class TestTheorem1LowerBound:
    """Theorem 1: top1_prob(tau) >= bound(Delta, n, tau)."""

    @pytest.mark.parametrize("n", [100, 1000, 50257])
    def test_no_violations(self, n: int):
        result = check_theorem_1(n=n, trials=200)
        assert result.passed, result.detail

    def test_gap_extreme_small(self):
        """Edge case: very small gap still respects bound."""
        n = 1000
        z = np.zeros(n)
        z[0] = 0.0
        z[1] = -0.01
        z[2:] = np.linspace(-1.0, -0.02, n - 2)
        for tau in [0.05, 0.1, 0.5, 1.0]:
            prob = top1_probability(z, tau)
            bound_val = 1.0 / (1.0 + (n - 1) * np.exp(-0.01 / tau))
            assert prob >= bound_val - 1e-12


class TestTheorem2Monotonicity:
    """Theorem 2: strictly decreasing in tau."""

    def test_strictly_decreasing(self):
        result = check_theorem_2(n=1000, trials=100)
        assert result.passed, result.detail

    def test_explicit_trend(self):
        n = 1000
        z = np.zeros(n)
        z[0] = 2.0
        z[1] = 0.0
        z[2:] = np.random.default_rng(501).standard_normal(n - 2) - 2.0
        taus = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
        probs = [top1_probability(z, t) for t in taus]
        for i in range(len(probs) - 1):
            assert probs[i] > probs[i + 1] + 1e-10

    def test_limit_uniform(self):
        """As tau -> inf, prob -> 1/n."""
        n = 1000
        z = np.random.default_rng(502).standard_normal(n)
        prob = top1_probability(z, tau=1e6)
        assert abs(prob - 1.0 / n) < 1e-4


class TestCorollary1Threshold:
    """Corollary 1: tau_alpha ensures prob >= alpha."""

    def test_passes(self):
        result = check_corollary_1(n=1000, trials=100)
        assert result.passed, result.detail

    @pytest.mark.parametrize("alpha", [0.8, 0.9, 0.95])
    def test_various_alpha(self, alpha: float):
        n = 5000
        delta = 2.0
        tau = threshold_temperature(delta, n, alpha)
        z = np.zeros(n)
        z[0] = 0.0
        z[1] = -delta
        z[2:] = np.random.default_rng(503).uniform(-3.0, -2.0, size=n - 2)
        prob = top1_probability(z, tau)
        assert prob >= alpha - 1e-3


class TestCorollary2Limit:
    """Corollary 2: tau -> inf yields uniform."""

    def test_passes(self):
        result = check_corollary_2(n=1000, trials=100)
        assert result.passed, result.detail


class TestCorollary3Shift:
    """Corollary 3: adding constant doesn't change probabilities."""

    def test_passes(self):
        result = check_corollary_3(n=500, trials=200)
        assert result.passed, result.detail

    @pytest.mark.parametrize("c", [-100.0, -1.0, 0.0, 1.0, 100.0])
    def test_specific_shifts(self, c: float):
        rng = np.random.default_rng(504)
        z = rng.standard_normal(500)
        p1 = tempered_softmax(z, tau=1.0)
        p2 = tempered_softmax(z + c, tau=1.0)
        assert np.max(np.abs(p1 - p2)) < 1e-12


class TestPredictionConservative:
    """Prediction: formula is conservative."""

    def test_passes(self):
        result = prediction_conservative_threshold()
        assert result.passed, result.detail
        assert result.metric > 0.0  # Positive margin
