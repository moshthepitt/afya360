/**
* PlaceController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('PlaceController', PlaceController)

  PlaceController.$inject = ['$scope', '$location', '$routeParams', 'Restangular', 'Meta'];

  /**
  * @namespace PlaceController
  */
  function PlaceController($scope, $location, $routeParams, Restangular, Meta) {
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

    Restangular.setDefaultRequestParams('get', {limit: 20, format: 'json'});

    var request_params = {
      limit: 20, 
      format: 'json',
      offset: 0
    }
    request_params[place_type] = place_id;

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
      Restangular.one(place_url_fragments[place_type], place_id).get().then(singlePlaceSuccessFn, singlePlaceErrorFn);      
    }

    /**
    * @name placeErrorFn
    * @desc Redirect to index
    */
    function placeErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('That place does not exist or does not have facilities.');
    }

    /**
    * @name facilitySuccessFn
    * @desc Update `facility` for view
    */
    function singlePlaceSuccessFn(data, status, headers, config) {
      vm.place = data;
      Meta.setTitle(vm.place.name + " " + vm.place.model_name);
    }

    /**
    * @name facilityErrorFn
    * @desc Redirect to index
    */
    function singlePlaceErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('That place does not exist.');
    }
  }
})();