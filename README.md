# ou-cyclicity
Cyclicity Analysis is the study of lead-lag dynamics amongst the components of a multivariate deterministic signal as it evolves throughout time.
Unlike many other methods for lead-lag analysis, Cyclicity Analysis is specifically time reparameterization invariant
i.e. its results are invariant under any continuous monotone transformation of the time axis.

The first part of Cyclicity Analysis is to construct the lead matrix corresponding to the given multivariate signal.
The lead matrix is a skew-symmetric matrix, in which the sign of the (i,j)th entry quantifies the extent to which the ith component leads (or lags) the jth component.
The second part of Cyclicity Analysis is to determine the temporal order of the components as the evolve throughout time
assuming the signal itself is periodic. In particular, under baseline assumptions, the structure of the leading eigenvector of the lead matrix
reflects the temporal order of the components.

In this project, we apply Cyclicity Analysis to the Multivariate Ornstein Uhlenbeck process, a stochastic process commonly used to model systems with mean-reverting behavior.
We consider a signal propagation model governed by the process: a one-dimensional signal propagates throughout a network of interconnected nodes, each represented by a component of the multivariate process.
We adapt Cyclicity Analysis to this stochastic setting and investigate its effectiveness in recovering the structure of the network.

# Installation

Requires Python 3.11 or higher.

```bash
pip install -r requirements.txt
```

Run the Jupyter notebook. 