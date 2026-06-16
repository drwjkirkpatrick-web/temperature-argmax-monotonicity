# Temperature Argmax Monotonicity Criterion

## Definitions

Let $\mathbf{z} \in \mathbb{R}^{n}$ be a logit vector with **sorted** values

$$
z_{(1)} \;\geq\; z_{(2)} \;\geq\; \cdots \;\geq\; z_{(n)}
$$

and assume a **strict maximum**: $z_{(1)} > z_{(2)}$. Define the **gap**

$$
\Delta \;:=\; z_{(1)} - z_{(2)} \;>\; 0.
$$

For temperature $\tau > 0$, the **tempered softmax** is

$$
\sigma_i(\tau) \;=\; \frac{\exp(z_i / \tau)}{\sum_{j=1}^{n} \exp(z_j / \tau)}.
$$

---

## Theorem 1 — Top-1 Probability Lower Bound

> Let $\Delta = z_{(1)} - z_{(2)} > 0$.  For all $\tau > 0$,
> $$
> \sigma_{(1)}(\tau)
> \;\geq\;
> \frac{e^{\Delta / \tau}}{e^{\Delta / \tau} + (n - 1)}.
> $$

---

## Theorem 2 — Strict Monotonicity of the Top-1 Probability

> The top-1 probability $\sigma_{(1)}(\tau)$ is **strictly decreasing** in $\tau$ on $(0, \infty)$.
> Moreover,
> $$
> \lim_{\tau \to 0^{+}} \sigma_{(1)}(\tau) = 1,
> \qquad
> \lim_{\tau \to \infty} \sigma_{(1)}(\tau) = \frac{1}{n}.
> $$

---

## Corollary 1 — Deterministic-Threshold Temperature (Edge-AI Criterion)

> For any confidence target $\alpha \in (1/n, 1)$, define
> $$
> \tau_{\alpha}
> \;:=\;
> \frac{\Delta}{\displaystyle\ln\!\Bigl(\frac{(n-1)\,\alpha}{1-\alpha}\Bigr)}.
> $$
> Then for all $\tau \leq \tau_{\alpha}$,
> $$
> \sigma_{(1)}(\tau) \;\geq\; \alpha.
> $$
>
> **Practical edge implication:** If a quantized edge model produces logits with typical gap $\Delta \approx 2$ (after $1/\sqrt{d_{\text{head}}}$ scaling), then with $n = 50{,}257$ (GPT-2 vocab) and target $\alpha = 0.9$:
> $$
> \tau_{0.9}
> \;=\;
> \frac{2}{\ln\bigl(50{,}256 \times 9\bigr)}
> \;\approx\;
> \frac{2}{13.0}
> \;\approx\; 0.15.
> $$
> Thus **temperatures below 0.15** guarantee >90% confidence in the top token, suitable for latency-critical edge generation.

---

## Corollary 2 — Minimum Temperature to Escape Determinism

> Conversely, to guarantee the top-1 probability stays **below** $\beta \in (1/n, 1)$, it suffices that
> $$
> \tau \;\geq\; \tau^{\beta}
> \;:=\;
> \frac{\Delta}{\displaystyle\ln\!\Bigl(\frac{(n-1)\,\beta}{1-\beta}\Bigr)}.
> $$
> For the same GPT-2 example with $\Delta = 2$ and $\beta = 0.5$:
> $$
> \tau^{0.5}
> \;=\;
> \frac{2}{\ln(50{,}256)}
> \;\approx\;
> \frac{2}{10.8}
> \;\approx\; 0.19.
> $$
> Temperatures above **0.19** force the top token to carry less than half the probability mass, promoting diversity.

---

## Corollary 3 — Non-Shift Invariance under Re-centering

> Adding a constant $c$ to all logits does **not** change $\sigma_{(1)}(\tau)$.  Subtracting $z_{(1)}$ (centering at the maximum) leaves the gap $\Delta$ invariant.  Consequently the threshold formulas depend **only** on $\Delta$, not on the absolute logit scale.

---

## Empirical Predictions

1. For synthetic logits with known gap $\Delta = 2$ and $n = 50{,}257$, empirical evaluation of $\sigma_{(1)}(\tau)$ matches the lower bound of Theorem 1 within $10^{-4}$ for $\tau \in [0.05, 1.0]$.
2. The threshold temperature $\tau_{0.9}$ computed from the formula agrees with the bisection root of $\sigma_{(1)}(\tau) = 0.9$ to within $10^{-6}$.
3. For a real GPT-2 logits snapshot (or simulated proxy), the actual top-1 probability as a function of $\tau$ is bounded above by the Theorem 1 lower bound and below by 1.0, forming a predictable "confidence envelope."

---

## References

- Jang, E., Gu, S., & Poole, B. (2017). Categorical Reparameterization with Gumbel-Softmax. *ICLR*.
- Maddison, C. J., Mnih, A., & Teh, Y. W. (2017). The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables. *ICLR*.
- Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020). The Curious Case of Neural Text Degeneration. *ICLR* (temperature sampling analysis).
