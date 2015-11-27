/**
* PlaceController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('PlaceController', PlaceController)

  PlaceController.$inject = ['$scope', '$location', '$routeParams', 'Restangular'];

  /**
  * @namespace PlaceController
  */
  function PlaceController($scope, $location, $routeParams, Restangular) {
    var vm = this; 

    var place_type = $routeParams.type;
    var place_id = $routeParams.id;    

    var place_url_fragments = {
      province: 'provinces/',
      county: 'counties/',
      constituency: 'constituencies/',
      district: 'districts/',
      division: 'divisions/',
      location: 'locations/',
      sub_location: 'sub-locations/',
    }

    vm.next = next;
    vm.back = back;
    vm.can_go_back = false;
    vm.can_go_forward = true;

    Restangular.setBaseUrl('/api/v1');

    var request_params = {
      limit: 20, 
      format: 'json',
      offset: 0
    }
    request_params[place_type] = place_id;

    Restangular.setDefaultRequestParams('get', {format: 'json'});
    Restangular.setRequestSuffix('/');

    Restangular.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
      if (operation === 'getList') {        
        vm.can_go_back = data.previous;
        vm.can_go_forward = data.next;        
        var newResponse = data.results;
        return newResponse;
      }
      return data;
    });

    activate();

    function activate() {
      Restangular.all('health-facilities/').getList(request_params).then(placeSuccessFn, placeErrorFn);
    }  

    function next() {
      vm.offset += 20;
      request_params['offset'] = vm.offset;
      vm.facilities = Restangular.all('health-facilities/').getList(request_params).$object;  
    } 

    function back() {
      vm.offset = vm.offset - 20;
      request_params['offset'] = vm.offset;
      vm.facilities = Restangular.all('health-facilities/').getList(request_params).$object;
    }   

    /**
    * @name placeSuccessFn
    * @desc Update `place` for view
    */
    function placeSuccessFn(data, status, headers, config) {
      vm.facilities = data;
      vm.offset = 0;
      vm.place = Restangular.one(place_url_fragments[place_type], place_id).get().$object;
    }

    /**
    * @name placeErrorFn
    * @desc Redirect to index
    */
    function placeErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('That place does not exist.');
    }
  }
})();