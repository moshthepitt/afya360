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
    vm.submit = submit;

    var place_type = $routeParams.type;
    var place_id = $routeParams.id;  

    Meta.setLoading(false);  

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

    function submit() {
      if (vm.q === undefined || vm.q == null) {
        // do nothing
      }  else {
        $location.url('/search').search({q: vm.q});
      }
    } 

    function next() {
      vm.offset += 20;
      request_params['offset'] = vm.offset; 
      Meta.setLoading(false);
      Restangular.all('health-facilities/').getList(request_params).then(navSuccessFn, navErrorFn);
    } 

    function navSuccessFn(data, status, headers, config) {
      vm.facilities = vm.facilities.concat(data);   
      vm.facilities.next = data.next;
      Meta.setLoading(true);
    }

    function navErrorFn(data, status, headers, config) {
      console.log('That place does not exist or does not have facilities.');
    } 

    function placeSuccessFn(data, status, headers, config) {
      vm.facilities = data;
      vm.offset = 0;      
      Restangular.one(place_url_fragments[place_type], place_id).get().then(singlePlaceSuccessFn, singlePlaceErrorFn);      
    }

    function placeErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('That place does not exist or does not have facilities.');
    }

    function singlePlaceSuccessFn(data, status, headers, config) {
      vm.place = data;
      Meta.setLoading(true);
      Meta.setTitle(vm.place.name + " " + vm.place.model_name + " | Afya360");
    }

    function singlePlaceErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('That place does not exist.');
    }
  }
})();