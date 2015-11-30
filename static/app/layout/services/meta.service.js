(function () {
  'use strict';

  angular
    .module('afya360.layout.services')
    .factory('Meta', Meta);

  function Meta(){
  	var title = "Afy360 | Kenya Directory of Health Centers";

  	return {
  		title: function() { return title; },
  		setTitle: function(new_title) {
  			title = new_title;
  		}
  	};
  }
})();