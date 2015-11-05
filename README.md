# Duplicator i3 Calibration

This project is my attempt to improve the quality of my Wanhoa
Duplicator printer.

I get obsessed with optimization and this is the result of that obsession.

# Links

* [Make 3DP test scoring](http://makezine.com/2014/11/07/how-to-evaluate-the-2015-make-3dp-test-probes/)

# Modifications

* [Glass Bed](http://www.amazon.com/gp/product/B00QQ5Q3BI?psc=1&redirect=true&ref_=oh_aui_detailpage_o01_s01)
* [Y Idler Zip Tie](http://3dprinterbrain.com/uploads/DupI3/RecommendedMods/YIdlerZip.jpg)
* [Thumbwheels](http://www.thingiverse.com/thing:874155)
* [Cobra Cooler](http://www.thingiverse.com/thing:1090433)
* Removed belt tensioner and tightened belt

# Build Notes
* 2015-10-30T11 - make/dimensional_accuracy_test.stl
  * 
* 2015-10-30T10 - make/XY_resonance_test.stl
  * I fixed the brittle walls by setting the steps/mm to 105
  * When the fan kicked on, the temp dropped 10-20c and the extruder
    started skipping
  * I set the ex temp to 210 to compensate for the fan and this
    stopped most of the skipping
* 2015-10-30T03
  * Put stock extruder gear back on because the D4 gear skipped too much
* 2015-10-29T19 - make/XY_resonance_test.stl
  * Brittle walls, gaps in layers
* 2015-10-29T18 -
  * Score=3
* 2015-10-29T17 - make/negative_space_tolerance_test.stl
  * Score=4
* 2015-10-29T16 - make/overhang_test.stl
  * ringing on the letters
  * 190c instead of 200c
  * I could hear the extruder gear skipping a step at the same X,Y cords
    regardless of Z. There's no visible artifact of this as far as I can tell.
  * Layer gap on the brim of the base
  * Score=4
* 2015-10-29T15 - make/bridging_test.stl
  * Score=5
* 2015-10-29T12 - make/dimensional_accuracy_test.stl
  * Replaced the DiiCooler with the rear mounted Cobra Cooler because the DiiCooler blocked the view and dropped the extruder temp by 10c when turned on.
  * Extruder Temp appox 190c instead of the request 200c
  * Y=20.05mm, X=20.15mm, avg diff=0.1mm, score=4
* 2015-10-26T01:25 - Test_your_3D_printer_v2_0.48mm.stl
  * Corners lifted with the PLA settings and clean glass bed
  * Extruded Temp was set to 200c but averaged around 180c


