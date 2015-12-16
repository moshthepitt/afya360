(function () {
  'use strict';

  angular
    .module('afya360.layout.services')
    .factory('Meta', Meta);

  function Meta(){
  	var title = "Afy360 | Kenya Directory of Health Facilities";
    var doneLoading = false;

  	return {
  		title: function() { return title; },
      doneLoading: function() { return doneLoading; },
  		setTitle: function(new_title) {
  			title = new_title;
  		},
      setLoading: function(new_loading_status) {
        doneLoading = new_loading_status;
      }
  	};
  }
})();