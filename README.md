# Morphological Scoring of Disease States
Many diseases are known to be connected to pathological changes in shape of anatomical organs. One prominent example is the neuro-degenerative Alzheimer's disease that we will focus upon during the hackathon. 

<img width="1248" alt="P3_intro_slide00" src="https://user-images.githubusercontent.com/73099411/158368624-204c5ddc-1931-49e5-b4e0-70f6a3d8940e.png">

Shapes can be represented in Riemannian shape spaces, we aim to obtain a classifier system that takes the non-Euclidean structure of shape spaces into account. 
The statistical shape model based approach [Ambellan et al. 2021](https://www.sciencedirect.com/science/article/abs/pii/S1361841521002243?via%3Dihub) ([arxiv](https://arxiv.org/pdf/2111.06850.pdf)) will serve as a starting point. Possible extensions include different metrics (e.g. **[Log-Cholesky](https://epubs.siam.org/doi/pdf/10.1137/18M1221084?casa_token=QpmKlgG0Qu4AAAAA:xyeYpohx-FxZsvQ4_EfsxmUsB_QYLW70sbxIRY6Bpo7FiXYrEGHDtSgabiizm1ud2d7OI2yDVjk)**), advanced Riemannian mean-variance analysis, robust estimators for centrality (e.g. **[med](https://www.sci.utah.edu/publications/fletcher08/Fletcher_CVPR2008.pdf)-[ian](https://openresearch-repository.anu.edu.au/bitstream/1885/13303/2/Aftab%20et%20al%20Generalized%20Weiszfeld%20Algorithms%202015.pdf)**), and intrinsic machine learning approaches (e.g. **[manifold support vector machine](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.329.9304&rep=rep1&type=pdf)**). However, the project is open to ***your*** ideas and whatever serves the purpose.

<img width="1248" alt="P3_intro_slide01" src="https://user-images.githubusercontent.com/73099411/158371878-8b2471e6-64e2-4d91-9bcb-f5e73da02af1.png">

## Possible points to start at
In advance it might be worth grasping some additional information:
* [GutHub Repo of TES Tandem Tutorial "Population wide Medical Image and Shape Analysis" (Tutorial 2)](https://github.com/ckolbPTB/TES_21_22_Tutorials). Attention: The Mybinder server takes approx. 10min. to start, don't worry about it. Besides the code examples you can also find some [slides](https://github.com/ckolbPTB/TES_21_22_Tutorials/blob/main/tutorial2_pop_med_image_shape_ana/Math%2B_TES_Tut2_Shape_Ana.pdf).
* [Morphomatics Library](https://morphomatics.github.io)
* [Update slides](https://docs.google.com/presentation/d/1vkxMv1EDZvgpK3wiMq2OvEySKp9yLgTMvYxdTGlk3GE/edit?usp=sharing)
