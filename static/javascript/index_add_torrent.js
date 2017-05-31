
// Call for to add torrent

function addTorrent()
{
    $.ajax({
        url: 'AddTorrent',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'newurl': getFieldValue('newurl')}),
        dataType:'json',
        beforeSend: function() {
            $('#ajaxloader').show();
        },
        success: function(data)
        {
            window.location.replace("/Torrent="+data.newtorrentid);
        },
        complete: function(){
            $('#ajaxloader').hide();
        }
    });
};
