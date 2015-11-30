(function () {
  'use strict';

  angular
    .module('afya360.config')
    .config(config);

  config.$inject = ['$locationProvider', 'RestangularProvider'];

  function config($locationProvider, RestangularProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');

    RestangularProvider.setBaseUrl('/api/v1');
    RestangularProvider.setDefaultRequestParams('get', {limit: 20, format: 'json'});
    RestangularProvider.setRequestSuffix('/');
    RestangularProvider.setDefaultHttpFields({cache: true});

    RestangularProvider.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
      var extractedData;
      if (operation === 'getList') { 
        extractedData = data.results;
        extractedData.count = data.count;
        extractedData.next = data.next;
        extractedData.previous = data.previous;
      } else {
      	extractedData = data;	
      }
      return extractedData;
    });
  }
  
})();