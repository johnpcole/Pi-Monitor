function updateTorrentTileColour(tileid, torrentstatus)
{
    var selectedcolour = "#FFFFFF";
    if ((torrentstatus == "downloading_active") || (torrentstatus == "downloading_queued")) {
        selectedcolour = "#DC6E00";
    } else if (torrentstatus == "downloading_paused") {
        selectedcolour = "#964B00";
    } else if ((torrentstatus == "seeding_active") || (torrentstatus == "seeding_queued")) {
        selectedcolour = "#009600";
    } else if (torrentstatus == "seeding_paused") {
        selectedcolour = "#003200";
    } else if (torrentstatus == "checking") {
        selectedcolour = "#4B0000";
    } else if (torrentstatus == "error") {
        selectedcolour = "#AF0000";
    } else {
        selectedcolour = "#FFFFFF";
    };
    changeAreaColour(tileid, selectedcolour);
};



function updateFileTileColour(tileid, filetype, fileoutcome)
{
    var selectedcolour = "#FFFFFF";
    if (filetype == "video") {
        if (fileoutcome == "copy") {
            selectedcolour = "#AFAF00";
        } else {
            selectedcolour = "#4B4B00";
        };
    } else if (filetype == "subtitle") {
        if (fileoutcome == "copy") {
            selectedcolour = "#000096";
        } else {
            selectedcolour = "#000032";
        };
    } else {
        selectedcolour = "#101010";
    };
    changeAreaColour(tileid, selectedcolour);
};
