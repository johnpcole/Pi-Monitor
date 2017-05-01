
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

function setFileConfigFields(torrenttype)
{
    var areaobjectlist = document.getElementsByClassName('copyonlyfields');
    var areaindex;
    var fileid;
    var fieldvalue;

    for (areaindex = 0; areaindex < areaobjectlist.length; areaindex++) {
        areaobject = areaobjectlist[areaindex];
        fileid = (areaobject.id).substring(11);
        episodevalue = getText("fileepisode-"+fileid);
        if (episodevalue == 'Ignored') {
            changeFileDesignation(fileid,'ignore');
        } else {
            if (torrenttype == "tvshow") {
                if (episodevalue.substring(0,9) == "Episodes ") {
                    episodeselection = "Ep. "+episodevalue.substring(9);
                } else {
                    episodeselection = episodevalue;
                };
                setFieldValue('episodeselector-'+fileid, episodeselection);
            };
            if (getImageName('filetype-'+fileid) == "subtitle") {
                setFieldValue('subtitleselector-'+fileid, getText("filesubtitle-"+fileid));
            };
            changeFileDesignation(fileid,'copy');
        };
    };
};
