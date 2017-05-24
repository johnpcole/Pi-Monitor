
// Ajax call for tv show seasons list

function updateTVShowSeasons(selectedseason)
{
    changeControlState('tvshowseasonselector', 'Hide');
    var tvshowname = getFieldValue("tvshowselector");
    if (tvshowname != "") {
        $.ajax({
            url: 'GetTVShowSeasons',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({'tvshow':tvshowname}),
            dataType:'json',
            beforeSend: function() {
                $('.ajaxloader').show();
            },
            success: function(data){
                updateTVShowSeasonsList(data.seasons, selectedseason);
            },
            complete: function(){
                $('.ajaxloader').hide();
            }
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


