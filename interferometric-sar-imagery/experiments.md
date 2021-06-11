## Experiments

### Logan Williams, June 10 2021
#### Blast/impact crater mapping

Can InSAR images be useful for mapping of deformations caused by airstrikes? I tried following the [University of Alaska's guide](https://asf.alaska.edu/how-to/data-recipes/create-an-interferogram-using-esas-sentinel-1-toolbox/) to generating an InSAR image using two Sentinel-1 passes from May 8 2021 and May 20 2021 in the Gaza Strip.

Results were not encouraging. Displacement was only non-zero in some areas, and it did not appear to represent real damage on the ground. Additionally, the non-zero displacement was mostly measured in areas with low phase coherence, indicating that the data is pretty suspect to begin with.

![](images/2021-06-10/displacement.png)

This failed for possibly several reasons.

- Coherence was generally low in the Gaza Strip area. This was especially true in many of the agricultural areas, as somewhat expected. This could have caused the phase unwrapping to fail entirely.
- Any significant impact sites would likely significantly change the radar reflection, guaranteeing incoherence.

That said, areas with destruction reported by UNITAR did _not_ appear to show low coherence. They actually seem to correlate with higher coherence, as is typical of urban areas. I don't currently have an explanation for this. The quick overlay below shows areas (in red) that have reported damage, and is brighted in areas with high coherence.

![](images/2021-06-10/gaza-sar.jpg)

- The changes in elevation expected as a result of an airstrike could be quite large, possibly above the "altitude of ambiguity," where phase unwrapping becomes more difficult if not impossible.

Other observations

- A radio installation near the Egypt/Gaza border is very visible in the imagery.

Overall: maybe there is some way to make this work, but it seems difficult and like it would have few advantages over conventional visible/infrared imagery. 
