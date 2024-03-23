# Unsupervised-GFANC: Unsupervised Learning Based End-to-End Delayless Generative Fixed-Filter Active Noise Control

This repository contains the code for the paper "**Unsupervised Learning Based End-to-End Delayless Generative Fixed-Filter Active Noise Control**," accepted by the 2024 IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP 2024). The paper is available on [ArXiv](https://arxiv.org/pdf/2402.09460.pdf) and [IEEE Xplore](https://ieeexplore.ieee.org/document/10448277).

<p align="center">
  <img src="https://github.com/Luo-Zhengding/Unsupervised-GFANC/assets/95018034/3a4c1258-2ac4-4078-89df-9a72b43a160e" width="400" height="300">
  <img src="https://github.com/Luo-Zhengding/Unsupervised-GFANC/assets/95018034/05f65a18-b5dd-4286-a9d0-5d1309aa62c8" width="400" height="300">
</p>

## Highlights

1. **Simplified Training Process**: The 1D CNN in our unsupervised-GFANC method does not require initial training using labelled noise data, simplifying the training process and enhancing practicality.
2. **End-to-End Differentiable ANC System**: Integrating the co-processor and real-time controller into the ANC system allows for using the accumulated squared error signal as the loss for training the 1D CNN.
3. **Improved Noise Reduction Performance**: The unsupervised-GFANC method exhibits better noise reduction performance than the supervised-GFANC method by avoiding labelling errors.

## Usage

1. **Pre-trained Model**: If you don't want to retrain the 1D CNN (`M5_Network.py`), you can use the trained model available in `models/1DCNN_SyntheticDataset_UnsupervisedLearning.pth`. Simply run the `Noise_Cancellation_RealNoise_RealPath.ipynb` notebook to get the noise reduction results.
2. **Training Dataset**: The 1D CNN is trained using a synthetic noise dataset with label files `Soft_Index.csv`. The entire dataset is available [here](https://drive.google.com/file/d/1hs7_eHITxL16HeugjQoqYFTs-Cm7J-Tq/view?usp=sharing).
3. **Applying to New Acoustic Paths**: We have provided the sub control filters on synthetic acoustic paths and our measured acoustic paths. If you want to use the Unsupervised-GFANC method on new acoustic paths, just obtain the corresponding pre-trained broadband control filter and decompose it into sub control filters. The trained 1D CNN in Unsupervised-GFANC can remain unchanged. For more details, please refer to the paper.

## Related Works

- [Deep Generative Fixed-Filter Active Noise Control](https://arxiv.org/pdf/2303.05788)
- [Delayless Generative Fixed-filter Active Noise Control based on Deep Learning and Bayesian Filter](https://ieeexplore.ieee.org/document/10339836/)
- [GFANC-Kalman: Generative Fixed-Filter Active Noise Control with CNN-Kalman Filtering](https://ieeexplore.ieee.org/document/10323505)
- [A hybrid sfanc-fxnlms algorithm for active noise control based on deep learning](https://arxiv.org/pdf/2208.08082)
- [Performance Evaluation of Selective Fixed-filter Active Noise Control based on Different Convolutional Neural Networks](https://arxiv.org/pdf/2208.08440)

**If you are interested in our works, please consider citing our papers. Thanks for your interest, and have a great day!**
