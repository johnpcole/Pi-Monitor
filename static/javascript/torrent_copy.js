// Invoke Torrent File Copy

function copyTorrent()
{
    var pathname = window.location.pathname;
    var torrentid = pathname.substring(9);
    changeButtonState('CloseCopy',"Disable");
    $('#copydialog').show();
    interactTorrentCopy(torrentid);
};


// Ajax call to get default edit fields

function interactTorrentCopy(torrentid)
{
    $.ajax({
        url: 'CopyTorrent',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'copyinstruction':torrentid}),
        dataType:'json',
        success: function(data){
            if (torrentid != "!!! CONTINUE EXISTING COPY PROCESS !!!") {
                populateCopyDialog(data.copydata);
            } else {
                updateCopyDialog(data.copydata);
            };
            if (data.refreshmode == true) {
                interactTorrentCopy("!!! CONTINUE EXISTING COPY PROCESS !!!");
            } else {
                changeButtonState('CloseCopy',"Enable");
            };
        }
    });
};


// Initial population of copy dialog

function populateCopyDialog(copydata)
{
    var outputtext = '';
    $.each(copydata, function(index)
    {
        var currentitem = copydata[index];
        outputtext = outputtext + '<div class="dialogitemleft dialogitem">' + currentitem.description + '</div>';
        outputtext = outputtext + '<div id="copydialog-' + index + '" class="dialogitemright dialogitem">';
        outputtext = outputtext + '&nbsp;<img src="./static/images/copy_' + currentitem.status + '.png" /></div>';
    });
    rerenderText('dialogcontent', outputtext);
};


// Update population of copy dialog

function updateCopyDialog(copydata)
{
    $.each(copydata, function(index)
    {
        var currentitem = copydata[index]
        currentobject = 'copydialog-' + index.toString()
        outputtext = ''
        if (currentitem.status != "queued") {
            if ((currentitem.description == "Connect File Server") || (currentitem.description == "Disconnect File Server")) {
                outputtext = outputtext + '(Attempt ' + currentitem.progress + ")"
            };
        };

        if (currentitem.status == "copying") {
            if ((currentitem.description != "Connect File Server") && (currentitem.description != "Disconnect File Server")) {
                outputtext = outputtext + '(~' + currentitem.progress + "%)"
            };
        };

        outputtext = outputtext + '&nbsp;<img src="./static/images/copy_' + currentitem.status + '.png" />';
        rerenderText(currentobject, outputtext);
    });
};




// Close torrent copy dialog

function closeCopyDialog()
{
    $('#copydialog').hide();
};
