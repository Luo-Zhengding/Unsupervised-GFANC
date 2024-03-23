# Unsupervised-GFANC: Unsupervised learning based end-to-end delayless generative fixed-filter active noise control

This is the code of the paper '**Unsupervised learning based end-to-end delayless generative fixed-filter active noise control**' accepted by 2024 IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP 2024). You can find the paper at [Arxiv](https://arxiv.org/pdf/2402.09460.pdf) or [Ieee xplore](https://ieeexplore.ieee.org/document/10448277).

<p align="center">
  <img src="https://github.com/Luo-Zhengding/Unsupervised-GFANC/assets/95018034/3a4c1258-2ac4-4078-89df-9a72b43a160e" alt="" width="400" height="300">
  <img src="https://github.com/Luo-Zhengding/Unsupervised-GFANC/assets/95018034/05f65a18-b5dd-4286-a9d0-5d1309aa62c8" alt="" width="400" height="300">
</p>
<p align="center">
</p>

**1.Highlights:**
(1) The 1D CNN in the previous supervised-GFANC method requires initial training using labelled noise data. Labelling noise data can be resource-intensive and may introduce some biases. In this paper, we propose an unsupervised-GFANC approach to simplify the 1D CNN training process and enhance its practicality.

(2) During training, the co-processor and real-time controller are integrated into an end-to-end differentiable ANC system. This enables us to use the accumulated squared error signal as the loss for training the 1D CNN.

(3) The unsupervised-GFANC method not only omits the labelling process but also exhibits better noise reduction performance than the supervised-GFANC method due to avioding labelling errors.

**2.How to use the code:**

(1) If you don't want to retrain the 1D CNN ('M5_Network.py'), the trained model can be found in 'models/[1DCNN_SyntheticDataset_UnsupervisedLearning.pth](https://github.com/Luo-Zhengding/Unsupervised-GFANC/blob/main/models/1DCNN_SyntheticDataset_UnsupervisedLearning.pth)', you can easily run the '[Noise_Cancellation_RealNoise_RealPath.ipynb](https://github.com/Luo-Zhengding/Unsupervised-GFANC/blob/main/Noise_Cancellation_RealNoise_RealPath.ipynb)' file to get the noise reduction results.

(2) The 1D CNN is trained using a synthetic noise dataset, its label files are 'Soft_Index.csv'. The entire dataset is available at https://drive.google.com/file/d/1hs7_eHITxL16HeugjQoqYFTs-Cm7J-Tq/view?usp=sharing

(3) We have provided the sub control filters on synthetic acoustic paths and real acoustic paths. If you want to use the Unsupervised-GFANC method on other new acoustic paths, just get the corresponding pre-trained broadband control filter and decompose it into sub control filters. Noticeably, the trained 1D CNN in the GFANC-Bayes system can remain unchanged. Detailed information can be found in the paper.

**Related works:**
- [Deep Generative Fixed-Filter Active Noise Control](https://arxiv.org/pdf/2303.05788)
- [Delayless Generative Fixed-filter Active Noise Control based on Deep Learning and Bayesian Filter](https://ieeexplore.ieee.org/document/10339836/)
- [GFANC-Kalman: Generative Fixed-Filter Active Noise Control with CNN-Kalman Filtering](https://ieeexplore.ieee.org/document/10323505)
- [A hybrid sfanc-fxnlms algorithm for active noise control based on deep learning](https://arxiv.org/pdf/2208.08082)
- [Performance Evaluation of Selective Fixed-filter Active Noise Control based on Different Convolutional Neural Networks](https://arxiv.org/pdf/2208.08440)
- **If you are interested in this work, you can read and cite our papers.**

Thanks for your reading! Have a nice day!
