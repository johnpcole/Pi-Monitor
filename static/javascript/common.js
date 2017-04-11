
// Update control visibility

function rerenderControl(controlname, displayvalue)
{
    var controlobject = document.getElementsByName(controlname)[0];
    if (displayvalue == 'Hide') {
        controlobject.style.display = "none";
    } else {
        controlobject.style.display = "inline";
    };
};



// Update area visibility

function rerenderArea(areaname, displayvalue)
{
    var areaobjectlist = document.getElementsByClassName(areaname);
    var areaindex;
    for (areaindex = 0; areaindex < areaobjectlist.length; areaindex++) {
        areaobject = areaobjectlist[areaindex]
        if (displayvalue == 'Hide') {
            areaobject.style.display = "none";
        } else {
            areaobject.style.display = "inline";
        };
    };
};



// Update the displayed data value

function rerenderText(fieldname, fieldvalue)
{
    var tileData = document.getElementById(fieldname);
    if (tileData != null) {
        tileData.innerHTML = fieldvalue;
    } else {
        alert("rerenderText: "+fieldname);
    };
};



// Get the displayed data value

function getText(fieldname)
{
    var tileData = document.getElementById(fieldname);
    if (tileData != null) {
        return tileData.innerHTML;
    } else {
        alert("getText: "+fieldname);
    };
};



// Update the displayed image

function rerenderImage(fieldname, fieldimage, fieldclass)
{
    var tileData = document.getElementById(fieldname);
    if (tileData != null) {
        tileData.innerHTML = "<img class=\""+ fieldclass +"\" src=\"/static/images/" + fieldimage + ".png\" alt=\"" + fieldimage + "\" />";
    } else {
        alert("rerenderImage: "+ fieldname);
    }
};



//Get field value

function getFieldValue(fieldname)
{
    return document.getElementsByName(fieldname)[0].value;
};



//Set field value

function setFieldValue(fieldname, fieldvalue)
{
    document.getElementsByName(fieldname)[0].value = fieldvalue;
};


