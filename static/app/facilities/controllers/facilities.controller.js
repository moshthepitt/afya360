/**
* FacilityController
* @namespace afya360.facilities.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.facilities.controllers')
  .controller('FacilityController', FacilityController)

  FacilityController.$inject = ['$scope', '$location', '$routeParams', 'Restangular'];

  /**
  * @namespace FacilityController
  */
  function FacilityController($scope, $location, $routeParams, Restangular) {
    var vm = this; 
    
    var id = $routeParams.id;    

    Restangular.setBaseUrl('/api/v1');
    Restangular.setDefaultRequestParams('get', {format: 'json'});
    Restangular.setRequestSuffix('/');

    activate();

    function activate() {
      Restangular.one('health-facilities', id).get().then(facilitySuccessFn, facilityErrorFn);
    }  

    /**
    * @name facilitySuccessFn
    * @desc Update `facility` for view
    */
    function facilitySuccessFn(data, status, headers, config) {
      vm.facility = data;
    }

    /**
    * @name facilityErrorFn
    * @desc Redirect to index
    */
    function facilityErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('That facility does not exist.');
    }
  }
})();