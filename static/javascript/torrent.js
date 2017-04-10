//Sets up the refresh when the page loads

$(document).ready(function ()
{
    updateControl('Edit', 'Show');

    // Refresh the tiles every minute.
    setInterval(function()
    {
        updateTorrent('Refresh');
    }, 10000);
});



// Ajax call for all torrent data

function updateTorrent(action)
{
    var pathname = window.location.pathname;
    $.getJSON('UpdateTorrent='+pathname.substring(9)+'='+action)
        .done(function (data)
        {
            if (action == 'Refresh') {
                updateTorrentTile(data.selectedtorrent);
            } else {
                updateTorrentConfig(data.selectedtorrent);
            };
        });
};



// Update the displayed data

function updateTorrentTile(dataitem)
{
    updateTorrentImage("Status", dataitem.status, "tilesubicon");
    updateTorrentData("Progress", dataitem.progress);
    updateTorrentData("SizeEta", "of "+dataitem.sizeeta);
};



// Update the displayed data for configured data

function updateTorrentConfig(dataitem)
{
    updateTorrentData("Sanitisedname", dataitem.sanitisedname);
};



// Update the displayed data value

function updateTorrentData(fieldname, fieldvalue)
{
    var tileData = document.getElementById(fieldname);
    if (tileData != null) {
        tileData.innerHTML = fieldvalue;
    } else {
        alert("updateTorrentData: "+fieldname);
    };
};


// Update the displayed image

function updateTorrentImage(fieldname, fieldimage, fieldclass)
{
    var tileData = document.getElementById(fieldname);
    if (tileData != null) {
        tileData.innerHTML = "<img class=\""+ fieldclass +"\" src=\"/static/images/" + fieldimage + ".png\" alt=\"" + fieldimage + "\" />";
    } else {
        alert("updateTorrentImage: "+ fieldname);
    }
};


// Edit torrent configuration

function editTorrentConfiguration()
{
    var itemdetails = document.getElementById('Sanitisedname').innerHTML;
    var itemsplit = itemdetails.split("   (");
    var moviename = itemsplit[0];
    var itemsplit = itemsplit[1].split(")");
    var movieyear = itemsplit[0];
    document.getElementsByName('moviename')[0].value = moviename;
    document.getElementsByName('movieyear')[0].value = movieyear;
    updateArea('edittextfields', 'Show');
    updateControl('Edit', 'Hide');
    updateControl('Save', 'Show');
};


// Save torrent configuration

function saveTorrentConfiguration()
{
    var moviename = document.getElementsByName('moviename')[0].value;
    var movieyear = document.getElementsByName('movieyear')[0].value;
    updateTorrent('Reconfigure|'+moviename+"|"+movieyear);
    updateArea('edittextfields', 'Hide');
    updateControl('Edit', 'Show');
    updateControl('Save', 'Hide');
};



// Update control visibility

function updateControl(controlname, displayvalue)
{
    var controlobject = document.getElementsByName(controlname)[0];
    if (displayvalue == 'Hide') {
        controlobject.style.display = "none";
    } else {
        controlobject.style.display = "inline";
    };
};


// Update area visibility

function updateArea(areaname, displayvalue)
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
