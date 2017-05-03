

// Edit torrent configuration

function editTorrentConfiguration()
{
    var moviename = getText('TorrentTitle')
    var movieyear = getText('TorrentSubtitle')
    var torrenttypeimagelabel = getImageName('TorrentType').substring(5);
    changeTorrentType(torrenttypeimagelabel);
    if (torrenttypeimagelabel == "movie") {
        setFieldValue('moviename', moviename);
        setFieldValue('movieyear', movieyear);
        setFileConfigFields(torrenttypeimagelabel);
    } else if (torrenttypeimagelabel == "tvshow") {
        setFieldValue('tvshowselector', moviename);
        updateTVShowSeasons(movieyear);
        setFileConfigFields(torrenttypeimagelabel);
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
    var newinstructions = {}
    if (newtype == 'tvshow') {
        newinstructions = { 'torrenttype' : newtype, 'tvshowname' : getFieldValue("tvshowselector"), 'season' : getFieldValue('tvshowseasonselector'), 'files' : getFileInstructions("tvshow") };
    } else if (newtype == 'movie') {
        newinstructions = { 'torrenttype' : newtype, 'moviename' : getFieldValue("moviename"), 'year' : getFieldValue('movieyear'), 'files' : getFileInstructions("movie") };
    } else {
        newinstructions = { 'torrenttype' : newtype, 'moviename' : getFieldValue("moviename") };
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
