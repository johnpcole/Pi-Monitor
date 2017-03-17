$(document).ready(function () {
    updateBuildTiles();

    // Refresh the tiles every minute.
    setInterval(function() {
        updateBuildTiles();
    }, 60000);
});





// Ajax call for all build tiles.
function updateBuildTiles() {
    $.getJSON('api/Build/GetStatus/' + id)
        .done(function (data) {
            processBuildResponse(data);
        });
    });
}





// Update the build tiles when ajax response is recieved.
function processBuildResponse(data) {
    var tile = document.getElementById(data.BuildDefinition);
    var tileStatus = tile.getElementsByClassName("status");
    var requestedBy = tile.getElementsByClassName("requested_by");
    var finishTime = tile.getElementsByClassName("finish_time");

    $(tileStatus).text("Build '" + data.BuildNumber + "' " + data.BuildStatus);
    $(requestedBy).text(data.RequestedBy);
    $(finishTime).text(data.FinishTime);
    var spinner = tile.getElementsByClassName("spinner");

    $(spinner).css("display", "none");
};