(function () {
  'use strict';

  angular
    .module('afya360.config')
    .config(config);

  config.$inject = ['$locationProvider'];

  function config($locationProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
  }

  // function config($resourceProvider) {
  //   $resourceProvider.defaults.stripTrailingSlashes = false;
  // }
})();