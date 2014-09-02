---
layout: post
title:	"Prove of Normal Equation"
date: 2014-08-31 10:16:00
categories: note
excerpt: "A prove of how Normal Equation works"
---

{% include custom/mathjax.html %}

###Preparation

--------------
We need to define some new symbols before we go on. These symbols are used by `Andrew Ng` in his open class in Stanford.

$$
{\bigtriangledown}_\theta = 
\begin{bmatrix}
\frac{\partial J}{\partial \theta_0}\\ 
...\\
\frac{\partial J}{\partial \theta_n}
\end{bmatrix}
$$

Thus \\(\theta_i := \theta_i - \alpha\bigtriangledown_\theta J\\)

For \\(f: \mathbb{R}^{m\times n}\rightarrow \mathbb{R}\\)

$$
{\bigtriangledown}_\theta f(A) = \begin{bmatrix}
\frac{\partial f}{\partial A_{11}} & ...  & \frac{\partial f}{\partial A_{1n}}  \\ 
 ...& ... &... \\ 
\frac{\partial f}{\partial A_{m1}} & ... & \frac{\partial f}{\partial A_{mn}}
\end{bmatrix}
$$

And some fact need to be recall here:
If \\(A\in\mathbb{R}^{n\times n} \\)

$$
tr(A) = \sum_{i=1}^{n}A_{ii} \\
tr(a) = a, a\in\mathbb{R}
$$

$$
tr(AB) = tr(BA) \\
tr(ABC) = tr(CAB) = tr(BCA)
$$

> The `trace` of a matrix will not change by taking the last one to the front.

Two more formulae related to `Partial Differential` of the trace matrix.
$$
{\bigtriangledown}_A tr(AB) = B^T
$$

And the most important one fact in this prove:

$$
{\bigtriangledown}_A tr(ABA^TC) = CAB + C^TAB
$$


###Prove

--------------
$$
{\bigtriangledown_\theta}J(\theta) \\
= \bigtriangledown_\theta \frac{1}{2}(X\theta - y)^T(X\theta - y) \\
= \frac{1}{2}\bigtriangledown_\theta(\theta^TX^TX\theta - \theta^TX^Ty - y^TX\theta + y^Ty) \\
= \frac{1}{2}\bigtriangledown tr(\theta\theta^TX^TX - \theta^TX^Ty - y^TX\theta) \\
= \frac{1}{2}[\bigtriangledown_\theta tr(\theta\theta^TX^TX) - \bigtriangledown_\theta tr(\theta^TX^Ty +y^TX\theta)]\\[3ex]
\because 
\theta^TX^Ty = (y^TX\theta)^T\\[3ex]
\therefore
{\bigtriangledown_\theta}J(\theta) = \frac{1}{2}[\bigtriangledown_\theta tr(\theta\theta^TX^TX) - 2\bigtriangledown_\theta tr(y^TX\theta)]\\[3ex]
\because
\bigtriangledown_\theta tr(\theta\theta^TX^TX) \\
= \bigtriangledown_\theta tr(\theta I \theta^TX^TX)\\
= X^TX\theta + X^TX\theta\\
= 2X^X\theta\\[3ex]
\bigtriangledown_\theta tr(y^TX\theta) = X^Ty\\[3ex]
\therefore
{\bigtriangledown_\theta}J(\theta)  = X^TX\theta - X^Ty \overset{set}{=} \overrightarrow{0}\\
\Rightarrow X^TX\theta \overset{set}{=} X^Ty
$$

Normal Equation proved!