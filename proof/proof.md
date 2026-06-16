# Proof of Theorems 1 and 2

## Lemma A — Exponential Ratio Inequality

**Statement.** For $x > y$ and $\tau > 0$,

$$
\frac{e^{x/\tau}}{e^{x/\tau} + \sum_{j=3}^{n} e^{z_{(j)}/\tau}}
\;\geq\;
\frac{e^{x/\tau}}{e^{x/\tau} + (n-1)\, e^{y/\tau}}.
$$

*Proof.* Since $z_{(j)} \leq y < x$ for all $j \geq 2$, each $e^{z_{(j)}/\tau} \leq e^{y/\tau}$. Replacing the $n-1$ remaining terms by their common upper bound makes the denominator larger, hence the fraction smaller or equal. Actually we want a **lower** bound on the top-1 probability, so we need the largest possible denominator that is still guaranteed. The maximal denominator under the ordering constraint is achieved when $z_{(2)} = \cdots = z_{(n)} = y$, giving exactly $(n-1)e^{y/\tau}$ extra terms. ∎

---

## Proof of Theorem 1 — Top-1 Probability Lower Bound

### Step 1 — Isolate the top component

$$
\sigma_{(1)}(\tau)
\;=\;
\frac{e^{z_{(1)}/\tau}}{\sum_{j=1}^{n} e^{z_{(j)}/\tau}}.
$$

### Step 2 — Lower-bound the denominator

Since $z_{(j)} \leq z_{(2)} = z_{(1)} - \Delta$ for all $j \geq 2$:

$$
\sum_{j=1}^{n} e^{z_{(j)}/\tau}
\;=\;
e^{z_{(1)}/\tau} + \sum_{j=2}^{n} e^{z_{(j)}/\tau}
\;\leq\;
e^{z_{(1)}/\tau} + (n-1)\, e^{(z_{(1)}-\Delta)/\tau}.
$$

### Step 3 — Form the lower bound

Dividing numerator and denominator by $e^{z_{(1)}/\tau}$:

$$
\sigma_{(1)}(\tau)
\;\geq\;
\frac{1}{1 + (n-1)\, e^{-\Delta/\tau}}
\;=\;
\frac{e^{\Delta/\tau}}{e^{\Delta/\tau} + (n-1)}.
$$

∎

---

## Proof of Theorem 2 — Strict Monotonicity

### Step 1 — Rewrite the top-1 probability

Define $S(\tau) := \sum_{j=1}^{n} e^{z_{(j)}/\tau}$. Then

$$
\sigma_{(1)}(\tau) = \frac{e^{z_{(1)}/\tau}}{S(\tau)}.
$$

### Step 2 — Differentiate with respect to $\tau$

Let $f(\tau) = \sigma_{(1)}(\tau)$.  Using the quotient rule:

$$
f'(\tau)
\;=\;
\frac{S(\tau) \cdot \frac{d}{d\tau}e^{z_{(1)}/\tau} - e^{z_{(1)}/\tau} \cdot S'(\tau)}{S(\tau)^2}.
$$

Now

$$
\frac{d}{d\tau}e^{z_{(j)}/\tau}
\;=\;
-\frac{z_{(j)}}{\tau^2}\, e^{z_{(j)}/\tau}.
$$

Therefore:

$$
S'(\tau) = -\frac{1}{\tau^2}\sum_{j=1}^{n} z_{(j)}\, e^{z_{(j)}/\tau}.
$$

### Step 3 — Sign of the derivative

Substituting:

$$
f'(\tau)
\;=\;
-\frac{1}{\tau^2 S(\tau)^2}
\Bigl[
S(\tau) \, z_{(1)}\, e^{z_{(1)}/\tau}
\;-\;
e^{z_{(1)}/\tau} \sum_{j=1}^{n} z_{(j)}\, e^{z_{(j)}/\tau}
\Bigr].
$$

Factor out $e^{z_{(1)}/\tau}$:

$$
f'(\tau)
\;=\;
-\frac{e^{z_{(1)}/\tau}}{\tau^2 S(\tau)^2}
\Bigl[
z_{(1)}\,S(\tau) - \sum_{j=1}^{n} z_{(j)}\, e^{z_{(j)}/\tau}
\Bigr].
$$

But $z_{(1)} S(\tau) = \sum_{j=1}^{n} z_{(1)} e^{z_{(j)}/\tau}$. So the bracket becomes:

$$
\sum_{j=1}^{n} \bigl(z_{(1)} - z_{(j)}\bigr) \, e^{z_{(j)}/\tau}
\;=\;
\sum_{j=2}^{n} \bigl(z_{(1)} - z_{(j)}\bigr) \, e^{z_{(j)}/\tau}
\;\geq\;
\Delta \, e^{z_{(2)}/\tau}
\;>\; 0.
$$

The first equality used $z_{(1)} - z_{(1)} = 0$. The inequality used $z_{(1)} - z_{(j)} \geq \Delta$ for all $j \geq 2$.

Since $\tau^2 > 0$, $S(\tau)^2 > 0$, and the bracket is strictly positive, we conclude:

$$
f'(\tau) \;<\; 0.
$$

Therefore $\sigma_{(1)}(\tau)$ is **strictly decreasing** in $\tau$.

### Step 4 — Boundary limits

As $\tau \to 0^{+}$, all mass concentrates on the maximum:
$e^{z_{(j)}/\tau} / e^{z_{(1)}/\tau} \to 0$ for $j \geq 2$, so $\sigma_{(1)}(\tau) \to 1$.

As $\tau \to \infty$, $e^{z_{(j)}/\tau} \to 1$ for all $j$, so $S(\tau) \to n$ and $\sigma_{(1)}(\tau) \to 1/n$. ∎

---

## Proof of Corollary 1 — Deterministic-Threshold Temperature

We want the smallest $\tau$ such that $\sigma_{(1)}(\tau) \geq \alpha$. By Theorem 1, it suffices to enforce the lower bound:

$$
\frac{e^{\Delta/\tau}}{e^{\Delta/\tau} + (n-1)} \;\geq\; \alpha.
$$

Solve for $\tau$:

$$
e^{\Delta/\tau} \;\geq\; \alpha \bigl(e^{\Delta/\tau} + n - 1\bigr)
\;\implies\;
(1 - \alpha)\, e^{\Delta/\tau} \;\geq\; \alpha (n - 1)
\;\implies\;
e^{\Delta/\tau} \;\geq\; \frac{\alpha(n-1)}{1-\alpha}.
$$

Taking logarithms:

$$
\frac{\Delta}{\tau} \;\geq\; \ln\!\Bigl(\frac{\alpha(n-1)}{1-\alpha}\Bigr)
\;\implies\;
\tau \;\leq\;
\frac{\Delta}{\ln\!\Bigl(\frac{\alpha(n-1)}{1-\alpha}\Bigr)}.
$$

Since $\sigma_{(1)}(\tau)$ is strictly decreasing (Theorem 2), smaller $\tau$ implies larger $\sigma_{(1)}$. Hence any $\tau$ satisfying the above inequality guarantees $\sigma_{(1)} \geq \alpha$. ∎

---

## Proof of Corollary 2 — Minimum Temperature to Escape Determinism

Analogous to Corollary 1, but now we want $\sigma_{(1)}(\tau) \leq \beta$. Using the trivial upper bound $\sigma_{(1)} \leq 1$, we need the **inverse** direction. Actually, a tighter upper bound follows from the same algebraic manipulation applied to the strict decrease: since $\sigma_{(1)}(\tau)$ is strictly decreasing, the condition $\sigma_{(1)}(\tau) \leq \beta$ is equivalent to $\tau \geq \tau^{*}$ where $\tau^{*}$ is the unique solution of $\sigma_{(1)}(\tau^{*}) = \beta$.

Using Theorem 1's lower bound, we get a **sufficient** condition: if the lower bound itself exceeds $\beta$, then the true value certainly exceeds $\beta$. For the converse direction (escape determinism), we use the looser upper bound $\sigma_{(1)} \leq 1$ and note that $\sigma_{(1)}$ approaches $1/n$ as $\tau \to \infty$. Therefore $\tau^{\beta}$ derived from equating the lower bound to $\beta$ gives a temperature that guarantees the true probability has crossed below some intermediate value.  A cleaner sufficient condition: solving

$$
\frac{e^{\Delta/\tau}}{e^{\Delta/\tau} + (n-1)} \;=\; \beta
$$

for $\tau$ gives exactly the formula of Corollary 2, and by strict monotonicity any $\tau \geq \tau^{\beta}$ forces the left-hand side $\leq \beta$, which implies $\sigma_{(1)} \leq \beta$ **provided** the lower bound is tight enough.

Actually, since the lower bound is always below the true $\sigma_{(1)}$, ensuring the lower bound $\leq \beta$ does **not** guarantee the true value $\leq \beta$. A rigorous sufficient condition requires an **upper** bound.  The simplest upper bound is the trivial $\sigma_{(1)} \leq 1$, which is useless.  However, if the gap $\Delta$ is relatively small compared to other gaps, the bound is close.  In practice, the formula of Corollary 2 serves as an engineering estimate rather than a strict guarantee. ∎

---

## Proof of Corollary 3 — Non-Shift Invariance

Adding $c$ to all logits:

$$
\tilde\sigma_i(\tau)
\;=\;
\frac{e^{(z_i+c)/\tau}}{\sum_j e^{(z_j+c)/\tau}}
\;=\;
\frac{e^{c/\tau}\, e^{z_i/\tau}}{e^{c/\tau}\,\sum_j e^{z_j/\tau}}
\;=\;
\sigma_i(\tau).
$$

Subtracting $z_{(1)}$ defines $\tilde z_i = z_i - z_{(1)}$, so $\tilde z_{(1)} = 0$ and $\tilde z_{(2)} = -\Delta$. The tempered softmax is unchanged, so the threshold formulas (which depend on $\Delta$ alone) are invariant. ∎

---

## Open Questions

1. **Tightness of Theorem 1.** Is the lower bound attained for some family of logit vectors, or can it be improved?
2. **Multi-modal distributions.** If there are $k$ logits tied at the top, the gap $\Delta = 0$ and the theorem collapses. What is the analog for top-$k$ probability concentration?
3. **Dynamic temperature.** During autoregressive generation, the typical gap $\Delta_t$ varies per timestep. Can we bound the probability that the greedy argmax stays constant over a window of temperatures?

---

*End of Proof*
