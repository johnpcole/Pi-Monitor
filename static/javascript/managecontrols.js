
// Update control visibility

function changeControlState(controlname, displayvalue)
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


// Get Control Enabled/Disabled state

function getControlState(controlname)
{
    var controlobject = document.getElementsByName(controlname)[0];
    if (controlobject.style.display == 'none') {
        return "Hidden";
    } else if (controlobject.disabled == false) {
        return "Enabled";
    } else if (controlobject.disabled == true) {
        return "Disabled";
    } else {
        alert ("Unknown button state!")
    };
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


//Repopulates dropdown list

function repopulateDropDownList(fieldname, itemlist)
{
    var combobox = document.getElementsByName(fieldname)[0];
    var newoptions = '';
    $.each(itemlist, function(index)
    {
        newoptions = newoptions + '<option value=\"'+itemlist[index]+'\">'+itemlist[index]+'</option>';
    });
    combobox.innerHTML = newoptions;
};

/*
//Clear dropdown list

function clearDropDownList(fieldname)
{
    var combobox = document.getElementsByName(fieldname)[0];
    while (comboBox.options.length > 0)
    {
        comboBox.remove(0);
    };
};
*/


//Set dropdown value

function setDropDownValue(fieldname, fieldvalue)
{
    var combobox = document.getElementsByName(fieldname)[0];
    var itemcount = combobox.options.length;
    for (var i=0; i<itemcount; i++)
    {
        if (combobox.options[i].value == fieldvalue)
        {
            combobox.options[i].selected = true;
            break;
        };
    };
};
