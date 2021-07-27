# Papers

###### Digital Audio Recording Analysis The Electric Network Frequency Criterion
Probably first paper about ENF extraction from audio signals.
Using Frequency Domain Analysis.
Suggested approach:
* Using DCLive Forensics software.
* Down sample the evidence to 120 Hz. (with "Change Sample Rate / Resolution" function)
* Band-pass filter the audio with cut frequencies around 49 and 51 Hz (with "Band Pass Filter")
* Compute the spectrogram with a 4096 points FFT.
* Make a vertical zoom around 50 Hz.
* Compare with the ENF database. (Probably manually - eye balling spectrogram).

https://www.tracertek.com/media/pdf/an4.pdf

###### Applications of ENF criterion in forensic audio, video, computer and telecommunication analysis
Probably first paper about ENF extraction from audio signals describing 3 possible methods.
* Time/frequency domain spectrograms method consists on computing spectrograms
    * Visually compare questioned versus database ENF.
    * Useful especially for questioned versus database ENF date and time verification.
    * The fastest one (if we know exect recording time), is easy to be implemented.
    * Reveals the ENF components number.
    * For longer than 10–15 min recordings.
    * Indicates a non-authentic or non-duplicate evidence recording. 
    * Must be used before the other two in order to find out the ENF components number.
* Frequency domain 
    * Method means to compute FFT over short time windows.
    * Extract the maximum magnitude value around 50/60 Hz and compare questioned samples versus database ENF.
    * Can be applied to one ENF component recordings for questioned versus database ENF verification or for database searching in order to identify the questioned ENF recording date and time. 
    * Can also be used on more than one ENF component recordings in order to separate the ENF components and detect their chronological enter the evidence.
* Time domain analysis
    * Consists on zero-crosses measure.
    * One ENF component recordings only. 
    * For bigger than 44 kHz sampling frequencies and by implementing zero-crosses interpolation can become sampling frequency independent.
    * Can offer more useful detail than a frequency domain analysis. 
    * Applying a band-pass filter with 49–51 Hz cut frequencies, without down sampling the signal, one can separate the ENF waveform from the rest of the recording.
    * Possible to analyse the original quantification levels of the signal.
* Calculation degree of correlation between questioned ENF component and reference database ENF for search/verification purpose is used for the last two methods.

https://www.sciencedirect.com/science/article/abs/pii/S0379073806004312

###### Power Grid Estimation Using Electric Network Frequency Signals
Using XGBoost classifier with 95.21% and 99.07% precision when ENF signals have 480 and 1920 data points
https://www.hindawi.com/journals/scn/2019/1982168/

###### Location Forensics Analysis Using ENF Sequences Extracted from Power and Audio Recordings
Using multi-class SVM classiﬁer on audio recording with 81% precision of 60 Hz power grid audio samples and 77% precision of 50 Hz power grid audio samples.
https://www.researchgate.net/publication/338064951_Location_Forensics_Analysis_Using_ENF_Sequences_Extracted_from_Power_and_Audio_Recordings

###### Detecting the Presence of ENF Signal in Digital Videos: a Superpixel based Approach
In this paper, a superpixel based ENF detection algorithm for video is presented.
Short video clips of about 2 minutes-length and can be used.
The algorithm is able to operate independently of the source camera sensor type, CCD or CMOS and achieves a very high ENF signal presence detection accuracy for videos captured by both sensor types.
90% true positive rate with 5% False positive rate. Full ROC curve in article.
https://arxiv.org/pdf/1903.09884.pdf
  
###### Forensic analysis of digital audio recordings based on acoustic mains hum
https://ieeexplore.ieee.org/document/7495982/metrics#metrics

###### Exploiting Spatial Signatures of Power ENF Signal for Measurement Source Authentication
The maximum overall identification rate is above 95%. Using Random forest classifier. Locating power source from measured ENF in grid.
https://www.osti.gov/servlets/purl/1558521
  
###### ENF Signal Induced by Power Grid: A New Modality for Video Synchronization
Used ENF signal to synchronise video records from different recorded by different cameras located in the same house.
https://www.mast.umd.edu/files/paper_ENF/conf_paper12_ACMMM14.pdf
  
###### ENF recognition article summary with brief method description.
https://www.mast.umd.edu/research.php?t=enf
  
###### Information Forensics: An Overview of the First Decade - Anti-Forensics and Countermeasures.
https://ieeexplore.ieee.org/document/6515027?tp=&arnumber=6515027&queryText%3Dinformation%20forensics%20overview%20of%20first%20decade=
https://ieeexplore.ieee.org/document/6630051?tp=&arnumber=6630051&queryText%3Danti-forensics%20and%20countermeasures%20of=

###### “Seeing” ENF: Power-Signature-Based Timestamp for Digital Multimedia via Optical Sensing and Signal Processing
An analytical model based on an autoregressive process is also developed for ENF signals, and the effectiveness of using innovation sequences from the model for timestamp verification is demonstrated.
https://ieeexplore.ieee.org/document/6553242?tp=&arnumber=6553242&queryText%3Dpower%20signature%20based%20timestamp=

###### Spectrum Combining for ENF Signal Estimation.
No audio. Video ENF detection used.
https://ieeexplore.ieee.org/document/6557080?tp=&arnumber=6557080&queryText%3Dspectrum%20combining%20for%20enf=

###### Electric Network Frequency Analysis 2.0
Using Fourier transformation with correlation coefficient of the frequency snippet.
https://gridradar.net/en/blog/post/electric-network-frequency-analysis-20
  
###### Detecting Malicious False Frame Injection Attacks on Video Surveillance at the Edge using Electrical Network Frequency Signals
https://www.preprints.org/manuscript/201904.0004/v1/download

###### Forensic Research Using Grid Data
The basic approach to extract the 50/60Hz electric network frequency (or its harmonics) from the digital audio recordings and compare it against a reliable reference frequency database (here FNET database is used).
https://powerit.utk.edu/forensic_research.html

###### VIDEO RECORDINGS LOCALIZATION BASED ON ELECTRIC NETWORK FREQUENCY VARIATION.
With C and Matlab source code. Diploma thesis.
http://castor.det.uvigo.es:8080/xmlui/bitstream/handle/123456789/182/Vlad-Dragos%20Darau.pdf?sequence=1&isAllowed=y
 
###### INVISIBLE GEO-LOCATION SIGNATURE IN A SINGLE IMAGE
ENF method for image location detection.
https://people.engr.ncsu.edu/cwong9/docs/2018_ICASSP.pdf

###### Feasibility of using Electrical Network Frequency fluctuations to perform forensic digital audio authentication
C-program combined with a probe can be used to build the reference database.
Short-Time Fourier Transform method is intended for the ENF extraction of longer signals while our novel proposed use of the Autoregressive parametric method and our implementation of the zero-crossing approach tackle the case of shorter recordings. A Graphical User Interface (GUI) was developed to facilitate the process of extracting the ENF fluctuations. The whole process is tested and evaluated for various scenarios ranging from long to short recordings.
https://ruor.uottawa.ca/bitstream/10393/24383/3/El_Gemayel_Tarek_2013_thesis.pdf
  
###### Time-of-recording estimation for audio recordings. 
For example, compared with the recent DMA algorithm, our method achieves a relative error rate decrease of 86.86% (from 20.32% to 2.67%) and a speedup of 45× faster search response (41.0444 s versus 0.8973 s). 
https://www.sciencedirect.com/science/article/pii/S1742287617301883

###### Mechanisms estimation described in book.
https://books.google.cz/books?id=_WcaEAAAQBAJ&pg=PA123&lpg=PA123&dq=enf+power+grid+audio+video+application&source=bl&ots=w4PxXL9MGS&sig=ACfU3U2Sh-94m41cPwdoCY61O-66SPHd3g&hl=cs&sa=X&ved=2ahUKEwijh8Dx5eXxAhUBvaQKHe3JDw8Q6AEwCXoECAoQAw#v=onepage&q=enf%20power%20grid%20audio%20video%20application&f=false

###### Geographic Location Estimation from ENF Signals with High Accuracy. 
80% Accuracy for ENF signal location estimation using SVM.
http://home.ustc.edu.cn/~darksnip/Geographic%20Location%20Estimation%20from%20ENF%20Signals%20with%20High%20Accuracy.pdf

