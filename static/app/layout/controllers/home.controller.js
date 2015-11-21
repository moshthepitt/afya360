/**
* HomeController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('HomeController', HomeController)
  // .factory('Facility', FacilityFactory)

  HomeController.$inject = ['$scope', 'Restangular'];

  /**
  * @namespace HomeController
  */
  function HomeController($scope, Restangular) {
    var vm = this; 
    vm.next = next;

    Restangular.setBaseUrl('/api/v1');
    Restangular.setDefaultRequestParams('get', {limit: 20});

    Restangular.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
        if (operation === 'getList') {
            var newResponse = data.results;
            return newResponse;
        }
        return data;
    });

    activate();

    function activate() {
      vm.facilities = Restangular.all('health-facilities/').getList({offset:0}).$object;
      vm.offset = 0;
    }  

    function next() {
      vm.offset += 1;
      vm.facilities = Restangular.all('health-facilities/').getList({offset:vm.offset}).$object;
    }    
  }
})();