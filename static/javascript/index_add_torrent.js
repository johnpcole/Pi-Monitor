
// Call for to add torrent

function addTorrent()
{
    $.ajax({
        url: 'AddTorrent',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'newurl': getFieldValue('newurl')}),
        dataType:'json',
        success: function(data)
        {
            window.location.replace("/Torrent="+data.newid);
        }
    });
};
