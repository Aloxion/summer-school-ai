# General notes
The references and links collected here are containing general text books or
python references as well as reading suggestions for those who want to go
deeper in some of the topics touched in the lecture.

# Textbooks
  - Bishop, C. M. (1995). Neural networks for pattern
    recognition. Oxford university press.
  - Goodfellow, I., Bengio, Y., & Courville, A. (2016).
    Deep learning. MIT press.
  - Strang, G. (2019). Linear Algebra and Learning
    from Data. Wellesley Cambridge Press.
  - Sanei (2013), "Adaptive Processing of Brain Signals".
    Available via SDU's library, also [online](https://www.sdu.dk/en/bibliotek).

# Python help
  - [How to Think Like a Computer Scientist: Learning with Python 3](https://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/functions.html)
  - For specific functionality, please see the links below.

# EDF+ a Data Format for EEG
## The Standard
  - [EDF+ Specs](https://www.edfplus.info/specs/edftexts.html)
  - [EDF+ FAQ](https://www.edfplus.info/specs/edffaq.html)
  - [EDF+ Dowloads](https://www.edfplus.info/downloads/index.html)

## Accessing & Viewing EDF+ Data
  - [edfbrowser visualisation tool](https://www.teuniz.net/edfbrowser/)
  - [pyedflib library for reading edf data](https://github.com/holgern/pyedflib)
  - [pyedflib documentation](http://pyedflib.readthedocs.org/)


# EEG Data sets
There are many available data sets, in the introduction we only cover the [chbmit data set](https://physionet.org/content/chbmit/1.0.0/).


# Optional Further Reading & Function References
## Feature selection / importance with python
### Forward, backward selection
  - [Guide to feature selection](https://www.analyticsvidhya.com/blog/2020/10/a-comprehensive-guide-to-feature-selection-using-wrapper-methods-in-python/)
  - [SciKit documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html)

### A more comprehensive approach
Explaining feature influence, i.e., what the model does with specific
analytical tools, e.g., [lime](https://github.com/marcotcr/lime).


## EEG
### EEG Artifacts
  - [Common Artifacts During EEG Recording](https://www.ncbi.nlm.nih.gov/books/NBK390358/)
  - [Lateral eye movement](https://eegatlas-online.com/index.php/en/artifacts/lateral-eye-movement-guest)
  - [Iwasaki et al, 2005, Effects of eyelid closure, blinks, and eye movements on the electroencephalogram](https://www.sciencedirect.com/science/article/abs/pii/S138824570400416X)
  - [Slides on EEG Artifacts](https://www.slideshare.net/SudhakarMarella/eeg-artifacts-15175461)


### Brain wave bands
A [tutorial on computing the average bandpower of an EEG signal](https://raphaelvallat.com/bandpower.html) with python.

### EEG for absence epilepsy
  - [Yoshinaga et al, 2004, EEG in childhood absence epilepsy](https://www.seizure-journal.com/article/S1059-1311(03)00196-1/fulltext)
  - [Smith, 2005, EEG in the diagnosis, classification, and management of patients with epilepsy](https://jnnp.bmj.com/content/76/suppl_2/ii2)
  - [Matur et al, 2009, The evaluation of interictal focal EEG findings in adult patients with absence seizures](https://www.sciencedirect.com/science/article/pii/S1059131109000041), or in the literature folder.
  - [Juvenile Absence Epilepsy](https://www.chp.edu/our-services/brain/neurology/epilepsy/types/syndromes/juvenile-absence-epilepsy)
  - [Kaushik Majumdar et al, 2014, Synchronization Implies Seizure or Seizure Implies Synchronization?](https://link.springer.com/article/10.1007/s10548-013-0284-z)
  - Sanei, Adaptive Processing of Brain Signals, John Wiley & Sons, 2013.


## Filters
### (FIR) Filters
  - [Scipy docs on FIR filters](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html)
  - [Scipy Cookbook on FIR filters](https://scipy-cookbook.readthedocs.io/items/FIRFilter.html)
  - [Scipy docs on the signal processing module](https://docs.scipy.org/doc/scipy/reference/signal.html)
  - [A blog entry on EEG signal filtering with scipy](https://www.daanmichiels.com/blog/2017/10/filtering-eeg-signals-using-scipy/)
  - [Pitfalls of filtering the EEG signal](https://sapienlabs.org/pitfalls-of-filtering-the-eeg-signal/)

### Phase shift of filters
  - [Understanding linear phase filters](https://www.allaboutcircuits.com/technical-articles/understanding-linear-phase-filters/)
  - [Phase response of FIR filters](https://flylib.com/books/en/2.729.1/phase_response_of_fir_filters.html)
  - [Scipy docs on forward-backward filtering](https://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipy.signal.filtfilt.html)


## Windowing
  - [Scipy docs on window functions](https://docs.scipy.org/doc/scipy/reference/signal.windows.html)
  - [Wikipedia on windowing & spectral analysis](https://en.wikipedia.org/wiki/Window_function#Spectral_analysis)
  - [More details on range and resolution of the different windows](https://rfmw.em.keysight.com/wireless/helpfiles/89600B/WebHelp/Subsystems/gui/content/meassetup_resbw_windowtypes.htm)
  - [Windowing and FFT](https://www.oreilly.com/library/view/elegant-scipy/9781491922927/ch04.html)


## Autocorrelation: correlation decay and system dynamics
  - [Slipantschuk et al, 2013, On the relation between Lyapunov exponents and exponential decay of correlations](https://iopscience.iop.org/article/10.1088/1751-8113/46/7/075101/pdf)
  - [Slipantschuk et al, 2013, On correlation decay in low-dimensional systems](https://www.researchgate.net/publication/260973200_On_correlation_decay_in_low-dimensional_systems?enrichId=rgreq-a7591c5e492d5cc6ef6b5c845c9223ea-XXX&enrichSource=Y292ZXJQYWdlOzI2MDk3MzIwMDtBUzo2ODc0NTM4OTU2NTk1MjBAMTU0MDkxMzE4OTI0OQ%3D%3D&el=1_x_3&_esc=publicationCoverPdf)
