# EnronVisualization

<h3>Summary</h3>

This visualization is a report of my findings in Udacity's Machine Learning P5, Evaluation of the 
Enron Data.

One of my key findings from that report was the importance of stock features and relative 
unimportance of email features to predicting POI status in a supervised learning algorithm.

Here I present a visualization of stock values broken down into exercised and total by POI status,
mail sent and mail received by POI status, and then a circular display of the direction and number of
unique links between POI (red dots), non-POI (blue dots) and non-examined email addresses (gray dot).

<h3>Design</h3>

This design was inspired, originally, by Mike Bolstock's Heirarchical Ege Bundling demo. I wanted to convey the
path that corruption may have taken through the company. I also intended it to convey some of the challenges 
I experienced when trying to incorporate email data into my P5 feature set. I wanted the visualization to show 
the most predictive features clearly and quantitatively, and provide a sense of how much noise was present in 
the email data and why the intuitive connection between emails sent and rank in the company (and thus likelihood 
of POI status) did not hold up under scrutiny. 

<h3>Feedback Summary</h3>

    #1: "I like the circle, but can you hover over the dots to see what email account they belong to?
    Also, what about directionality? Are these multiple emails, who are they going to, and how would I know?"
    
    This first piece of feedback was from a friend with a background in design and pursuing a masters in 
    English. All I had at this point was a circle of dots, and lines between them. In response to this critique, 
    I added hover functionality to the dots, and decided to trim the data so that it reflected 
    unique connections only. Link lines were changed to darker when the sender is hovered, and links to "other" 
    are hidden when "other" is not hovered.
    
    #2: "What are the dots without lines telling me? How does this relate to your project, and what are you trying
    to explain with this visualization?"
    
    This feedback, from fellow Udacity student Michael DuPont, was the second draft of my visualization. Getting such 
    broad feedback on a second draft made me realize that just the links would not tell the full story. I added the 
    stock and email dimple charts as stacked bar charts.
    
    #3: "The transitions are too slow - how will I know they're going to change? Other could be a little more distinct,
    and the fact that so few POI's emailed eachother is very interesting. Maybe highlight that, after quantifying the 
    email features you used in the ML investigation."
    
    My last feedback came from a former math teacher and IT/business professional. To address these concerns, I changed
    the dot circle to just persons of interest, and made the "other" dot bigger. I edited the details in the financial 
    chart so that they were clearer and reflected the financial features, and added more text to make sure hover functionality
    was clear.
    
<h3>Resources</h3>
In addition to the Data Visualization course on Udacity, the following sources
were referenced:

The best d3.js tutorial ever:
http://alignedleft.com/ 
http://chimera.labs.oreilly.com/books/1230000000345/index.html
(his basic tutorial and his interactive, free, online book. all of it.)

working with json:
https://www.dashingd3js.com/d3-examples/1-d3-and-javascript-working-with-json
http://stackoverflow.com/questions/24007524/annoying-unicode-error-while-dumping-json

finding radius coordinates:
https://www.wyzant.com/resources/lessons/math/trigonometry/unit-circle
http://stackoverflow.com/questions/11336251/accessing-d3-js-element-attributes-from-the-datum
http://jsfiddle.net/cyril123/3uhv02z1/1/
http://stackoverflow.com/questions/33491344/how-to-access-d3-point-coordinates-after-transform
http://stackoverflow.com/questions/22360355/how-to-select-a-d3-svg-path-with-a-particular-id
http://bl.ocks.org/mbostock/3750558
https://spin.atomicobject.com/2015/06/12/objects-around-svg-circle-d3-js/

inspiration for radial graph:
http://mbostock.github.io/d3/talk/20111116/bundle.html

dimple ref:
http://mdupont.com/Programming/OPD-Data-Vis/
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.chart#addColorAxis
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.plot#bubble
https://github.com/PMSI-AlignAlytics/dimple/blob/master/data/example_data.tsv
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.series
http://dimplejs.org/advanced_examples_viewer.html?id=advanced_custom_styling
http://dimplejs.org/examples_viewer.html?id=bars_vertical_grouped_stacked
http://dimplejs.org/advanced_examples_viewer.html?id=advanced_lollipop_with_hover

javascript reference:
http://www.w3schools.com/js/js_if_else.asp
http://www.w3schools.com/js/js_comparisons.asp

quick lambda refresher for json construction:
http://stackoverflow.com/questions/1585322/is-there-a-way-to-perform-if-in-pythons-lambda
