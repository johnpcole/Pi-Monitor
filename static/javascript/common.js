
// Update control visibility

function rerenderControl(controlname, displayvalue)
{
    var controlobject = document.getElementsByName(controlname)[0];
    if (displayvalue == 'Hide') {
        controlobject.style.display = "none";
    } else if (displayvalue == 'Show') {
        controlobject.style.display = "inline";
    } else if (displayvalue == 'Enable') {
        controlobject.disabled = false;
    } else if (displayvalue == 'Disable') {
        controlobject.disabled = true;
    } else {
        alert ("Unknown button state: "+displayvalue)
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

function rerenderImage(fieldname, fieldimage)
{
    var tileData = document.getElementById(fieldname);
    if (tileData != null) {
        tileData.src = "/static/images/"+fieldimage+".png";
    } else {
        alert("rerenderImage: "+ fieldname);
    }
};



// Get displayed image filename

function getImageName(fieldname)
{
    var tileData = document.getElementById(fieldname);
    var outcome = "unknown"
    if (tileData != null) {
        var fullpath = tileData.src;
        var pathsplit = fullpath.split('/');
        var filename = pathsplit[pathsplit.length -1];
        outcome = filename.split('.')[0];
    } else {
        alert("GetImageName: "+ fieldname);
    }
    return outcome
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



//Set checkbox value

function setCheckboxValue(fieldname, fieldvalue)
{
    document.getElementsByName(fieldname)[0].checked = fieldvalue;
};



//Get checkbox value

function getCheckboxValue(fieldname)
{
    return document.getElementsByName(fieldname)[0].checked;
};
