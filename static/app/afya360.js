(function () {
	'use strict';

	angular
		.module('afya360', [
			'afya360.config',	
			'afya360.routes',
			'afya360.layout',
			'afya360.facilities',
			'restangular',
			'platypus.tabs',
			'ngSanitize'
		]);

	angular
		.module('afya360.config', ['restangular']);

	angular
		.module('afya360.routes', ['ngRoute']);

	angular
		.module('afya360')
		.run(run);

	run.$inject = ['$http'];

	/**
	* @name run
	* @desc Update xsrf $http headers to align with Django's defaults
	*/
	function run($http) {
	  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
	  $http.defaults.xsrfCookieName = 'csrftoken';
	}
})();