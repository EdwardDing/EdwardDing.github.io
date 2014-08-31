---
layout: post
title:	"Prove of Normal Equation"
data: 2014-08-31 10:16:00
categories: note
excerpt: "A prove of how Normal Equation works"
---

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

And some fact need to be recall here in