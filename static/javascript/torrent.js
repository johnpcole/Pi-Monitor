//Sets up the refresh when the page loads

$(document).ready(function ()
{
    rerenderControl('Edit', 'Show');

    // Refresh the tiles every minute.
    setInterval(function()
    {
        updateTorrentState('Refresh');
    }, 10000);
});



// Ajax call for all torrent downloading data

function updateTorrentState(action)
{
    var pathname = window.location.pathname;
    $.getJSON(action+'Torrent='+pathname.substring(9))
        .done(function (data)
        {
                updateTorrentStateDisplay(data.selectedtorrent);
        });
};


// Ajax call for all torrent configuration data

function updateTorrentConfig(action)
{
    var pathname = window.location.pathname;
    $.getJSON('ReconfigureTorrent='+pathname.substring(9)+'='+action)
        .done(function (data)
        {
                updateTorrentConfigDisplay(data.selectedtorrent);
        });
};




// Update the displayed data

function updateTorrentStateDisplay(dataitem)
{
    rerenderImage("Status", dataitem.status);
    rerenderText("Progress", dataitem.progress);
    rerenderText("SizeEta", "of "+dataitem.sizeeta);
};



// Update the displayed data for configured data

function updateTorrentConfigDisplay(dataitem)
{
    rerenderText("Sanitisedname", dataitem.sanitisedname);
};



// Edit torrent configuration

function editTorrentConfiguration()
{
    var itemdetails = getText('Sanitisedname');
    var itemsplit = itemdetails.split("   (");
    if (itemsplit.length > 1) {
        var moviename = itemsplit[0];
        var itemsubsplit = itemsplit[1].split(")");
        var movieyear = itemsubsplit[0];
    } else {
        var moviename = itemdetails
        var movieyear = ""
    };
    var torrenttypeimagelabel = getImageName('torrenttypeimage');
    changeTorrentType(torrenttypeimagelabel);
    setFieldValue('moviename', moviename);
    setFieldValue('tvshowselector', moviename);
    setFieldValue('movieyear', movieyear);
    rerenderArea('edittextfields', 'Show');
    rerenderControl('Edit', 'Hide');
    rerenderControl('Save', 'Show');
};


// Save torrent configuration

function saveTorrentConfiguration()
{
    var torrenttype = getImageName('torrenttypeimage');

    var currenttorrenttype = getImageName('torrenttypeimage')
    var moviename = ""
    if (currenttorrenttype == 'tvshow') {
        moviename = getFieldValue("tvshowselector");
    } else if (currenttorrenttype == 'movie') {
        moviename = getFieldValue("moviename");
    };
    var movieyear = getFieldValue('movieyear');
    updateTorrentConfig(torrenttype+'|'+moviename+'|'+movieyear);
    rerenderArea('edittextfields', 'Hide');
    rerenderControl('Edit', 'Show');
    rerenderControl('Save', 'Hide');
};


// Change torrent type

function changeTorrentType(newtype)
{
    if (newtype == "movie") {
        setFieldValue('moviename', '');
        rerenderControl('AddTVShow', "Hide");
        rerenderControl('tvshowselector', "Hide");
        rerenderControl('moviename', "Show");
        rerenderControl('movieyear', "Show");
        rerenderControl('MakeMovie', "Disable");
        rerenderControl('MakeTVShow', "Enable");
        rerenderControl('MakeUnknown', "Enable");
    } else if (newtype == "tvshow") {
        setFieldValue('tvshowselector', '');
        rerenderControl('AddTVShow', "Show");
        rerenderControl('tvshowselector', "Show");
        rerenderControl('moviename', "Hide");
        rerenderControl('movieyear', "Show");
        rerenderControl('MakeMovie', "Enable");
        rerenderControl('MakeTVShow', "Disable");
        rerenderControl('MakeUnknown', "Enable");
    } else {
        setFieldValue('moviename', '');
        setFieldValue('tvshowselector', '');
        setFieldValue('movieyear', '');
        rerenderControl('AddTVShow', "Hide");
        rerenderControl('tvshowselector', "Hide");
        rerenderControl('moviename', "Hide");
        rerenderControl('movieyear', "Hide");
        rerenderControl('MakeMovie', "Enable");
        rerenderControl('MakeTVShow', "Enable");
        rerenderControl('MakeUnknown', "Disable");
    };
    rerenderImage('torrenttypeimage', newtype);
};