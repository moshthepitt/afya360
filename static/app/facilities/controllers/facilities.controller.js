/**
* FacilityController
* @namespace afya360.facilities.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.facilities.controllers')
  .controller('FacilityController', FacilityController)

  FacilityController.$inject = ['$scope', '$location', '$routeParams', 'Restangular', 'Meta'];

  /**
  * @namespace FacilityController
  */
  function FacilityController($scope, $location, $routeParams, Restangular, Meta) {
    var vm = this; 
    vm.submit = submit;
    
    var id = $routeParams.id;    
    Meta.setLoading(false);

    Restangular.setBaseUrl('/api/v1');
    Restangular.setDefaultRequestParams('get', {format: 'json'});
    Restangular.setRequestSuffix('/');

    activate();

    function activate() {      
      Restangular.one('health-facilities', id).get().then(facilitySuccessFn, facilityErrorFn);
    }  

    function submit() {
      if (vm.q === undefined || vm.q == null) {
        // do nothing
      }  else {
        $location.url('/search').search({q: vm.q});
      }
    } 

    function facilitySuccessFn(data, status, headers, config) {
      vm.facility = data;
      Meta.setTitle(vm.facility.name + " | Afya360");
      Meta.setLoading(true);
    }

    function facilityErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('That facility does not exist.');
    }
  }
})();