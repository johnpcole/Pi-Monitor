//Sets up the refresh when the page loads

$(document).ready(function ()
{
    changeControlState('Edit', 'Show');

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



// Ajax call for tv show seasons list

function updateTVShowSeasons(selectedseason)
{
    changeControlState('tvshowseasonselector', 'Hide');
    var tvshowname = getFieldValue("tvshowselector");
    if (tvshowname != "") {
        $.getJSON('GetTVShowSeasons='+tvshowname)
            .done(function (data)
            {
                updateTVShowSeasonsList(data.seasons, selectedseason);
            });
    } else {
        updateTVShowSeasonsList("", selectedseason);
    };
    changeControlState('tvshowseasonselector', 'Show');
};


// Update the list of seasons in the dropdown list

function updateTVShowSeasonsList(seasonslist, selectedseason)
{
    repopulateDropDownList("tvshowseasonselector", seasonslist);
    setFieldValue('tvshowseasonselector', selectedseason)
};



// Update the displayed data

function updateTorrentStateDisplay(dataitem)
{
    rerenderImage("Status", "status_"+dataitem.status);
    rerenderText("Progress", dataitem.progress);
};



// Update the displayed data for configured data

function updateTorrentConfigDisplay(dataitem)
{
    rerenderText("TorrentTitle", dataitem.torrenttitle);
    rerenderText("TorrentSubtitle", dataitem.torrentsubtitle);
    rerenderImage("TorrentType", "type_"+dataitem.torrenttype);

    var filelist = dataitem.files;
    $.each(filelist, function(index)
    {
        rerenderText("filename-"+filelist[index].fileid, filelist[index].description);
        rerenderImage("outcome-"+filelist[index].fileid, "fileaction_"+filelist[index].outcome);
    });

};



// Edit torrent configuration

function editTorrentConfiguration()
{
    var moviename = getText('TorrentTitle')
    var movieyear = getText('TorrentSubtitle')
    if (movieyear.length > 3) {
        movieyear = movieyear.substring(3);
    };
    var torrenttypeimagelabel = getImageName('TorrentType').substring(5);
    changeTorrentType(torrenttypeimagelabel);
    if (torrenttypeimagelabel == "movie") {
        setFieldValue('moviename', moviename);
        setFieldValue('movieyear', movieyear);
        setFileConfigFields()
    } else if (torrenttypeimagelabel == "tvshow") {
        setFieldValue('tvshowselector', moviename);
        updateTVShowSeasons(movieyear);
        setFileConfigFields();
    };
    changeAreasState('editmodefields', 'Show');
    changeAreasState('readonlyfields', 'Hide');
    changeControlState('Edit', 'Hide');
    changeControlState('Save', 'Show');
};


// Save torrent configuration

function saveTorrentConfiguration()
{
    var newtype = ""
    if (getButtonState('MakeTVShow') == 'Disabled') {
        newtype = "tvshow";
    } else if (getButtonState('MakeMovie') == 'Disabled') {
        newtype = "movie";
    } else {
        newtype = "unknown";
    }
    var newinstructions = newtype
    if (newtype == 'tvshow') {
        newinstructions = newinstructions+"|"+getFieldValue("tvshowselector");
        newinstructions = newinstructions+"|"+getFieldValue('tvshowseasonselector');
        newinstructions = newinstructions+getFileInstructions("tvshow");
    } else if (newtype == 'movie') {
        newinstructions = newinstructions+"|"+getFieldValue("moviename");
        newinstructions = newinstructions+"|"+getFieldValue('movieyear');
        newinstructions = newinstructions+getFileInstructions("movie");
    } else {
        newinstructions = newinstructions+"|New Unspecified Torrent|";
    };
    updateTorrentConfig(newinstructions);
    changeAreasState('editmodefields', 'Hide');
    changeAreasState('readonlyfields', 'Show');
    changeControlState('Edit', 'Show');
    changeControlState('Save', 'Hide');
};


// Change torrent type

function changeTorrentType(newtype)
{
    if (newtype == "movie") {
        setFieldValue('moviename', '');
        setFieldValue('movieyear', '');
        changeAreasState('unknownonlyfields', "Hide");
        changeAreasState('tvshowonlyfields', "Hide");
        changeAreasState('movieonlyfields', "Show");
        changeButtonState('MakeMovie', "Disable");
        changeButtonState('MakeTVShow', "Enable");
        changeButtonState('MakeUnknown', "Enable");
    } else if (newtype == "tvshow") {
        setFieldValue('tvshowselector', '');
        setFieldValue('tvshowseasonselector', '');
        changeAreasState('unknownonlyfields', "Hide");
        changeAreasState('movieonlyfields', "Hide");
        changeAreasState('tvshowonlyfields', "Show");
        changeButtonState('MakeMovie', "Enable");
        changeButtonState('MakeTVShow', "Disable");
        changeButtonState('MakeUnknown', "Enable");
    } else {
        setFieldValue('moviename', '');
        setFieldValue('tvshowselector', '');
        setFieldValue('movieyear', '');
        setFieldValue('tvshowseasonselector', '');
        changeAreasState('unknownonlyfields', "Show");
        changeAreasState('tvshowonlyfields', "Hide");
        changeAreasState('movieonlyfields', "Hide");
        changeButtonState('MakeMovie', "Enable");
        changeButtonState('MakeTVShow', "Enable");
        changeButtonState('MakeUnknown', "Disable");
    };
};

// Change file designation

function changeFileDesignation(fileid, newtype)
{
    if (newtype == "ignore") {
        changeAreaState('copyconfig-'+fileid, "Hide");
        changeAreaState('ignoreconfig-'+fileid, "Show");
        changeButtonState('MakeIgnore-'+fileid, "Disable");
        changeButtonState('MakeCopy-'+fileid, "Enable");

    } else {
        changeAreaState('ignoreconfig-'+fileid, "Hide");
        changeAreaState('copyconfig-'+fileid, "Show");
        changeButtonState('MakeCopy-'+fileid, "Disable");
        changeButtonState('MakeIgnore-'+fileid, "Enable");
    };
};

// Get all File designations

function getFileDesignations()
{
    var fileinstructions = [];
    var areaobjectlist = document.getElementsByClassName('copyonlyfields');
    var areaindex;
    var fileid;
    var filetype;
    var subflag;

    for (areaindex = 0; areaindex < areaobjectlist.length; areaindex++) {
        areaobject = areaobjectlist[areaindex];
        fileid = (areaobject.id).substring(11);
        if (getButtonState('MakeIgnore-'+fileid) == 'Disabled') {
            fileinstructions.push([fileid, "ignore", "no-episode", "no-filetype", "no-subtitle"]);
        } else {
            filetype = (getImageName("filetype-"+fileid)).substring(9)
            if (filetype == "subtitle") {
                subflag = getFieldValue("subtitleselector-"+fileid)
            } else {
                subflag = "-"
            }
            fileinstructions.push([fileid, "copy", getFieldValue("episodeselector-"+fileid), filetype, subflag]);
        };
    };
    return fileinstructions
};

// Get sanitised tvshow & movie file designations

function getFileInstructions(torrenttype)
{
    var rawdata = getFileDesignations();
    var rawlength = rawdata.length;
    var loopindex;
    var currentitem;
    var outcome = ""
    for (loopindex = 0; loopindex < rawlength; loopindex++) {
        currentitem = rawdata[loopindex]
        outcome = outcome + "|" + currentitem[0]
        if (torrenttype == "movie") {
            currentitem[2] = "Film"
        };
        if ((currentitem[1] == "copy") && (currentitem[2] != "")) {
            outcome = outcome + "|" + currentitem[2]
            if ((currentitem[3] == "subtitle") && (currentitem[4] != "")) {
                outcome = outcome + "_" + currentitem[4]
            };
        } else {
            outcome = outcome + "|ignore"
        };
    };
    return outcome;
};



// Setup file config field states

function setFileConfigFields()
{
    var areaobjectlist = document.getElementsByClassName('copyonlyfields');
    var areaindex;
    var fileid;
    var fieldvalue;

    for (areaindex = 0; areaindex < areaobjectlist.length; areaindex++) {
        areaobject = areaobjectlist[areaindex];
        fileid = (areaobject.id).substring(11);
        fieldvalue = getText("filename-"+fileid);
        if (fieldvalue.substring(0, 6) == 'Ignore') {
            changeFileDesignation(fileid,'ignore');
        } else {
            changeFileDesignation(fileid,'copy');

        };
    };
};
