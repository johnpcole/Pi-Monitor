
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


