/**
* SearchController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('SearchController', SearchController)

  SearchController.$inject = ['$scope', '$location', '$routeParams', 'Restangular', 'Meta'];

  /**
  * @namespace SearchController
  */
  function SearchController($scope, $location, $routeParams, Restangular, Meta) {
    var vm = this; 
    vm.next = next;
    vm.submit = submit;

    Meta.setLoading(false);

    var query = $routeParams.q;
    var request_params = {
      limit: 20, 
      format: 'json',
      offset: 0
    }

    if (query === undefined || query == null) {
      // do nothing
    }  else {
      request_params['text'] = query;
    }

    Restangular.setDefaultRequestParams('get', {limit: 20, format: 'json'});

    activate();

    function activate() {
      Restangular.all('hf-search/').getList(request_params).then(searchSuccessFn, searchErrorFn);      
    }  

    function next() {
      vm.offset += 20;
      request_params['offset'] = vm.offset;
      Meta.setLoading(false); 
      Restangular.all('hf-search/').getList(request_params).then(navSuccessFn, navErrorFn);      
    }   

    function submit() {
      if (vm.q === undefined || vm.q == null) {
        // do nothing
      }  else {
        $location.url('/search').search({q: vm.q});
      }
    } 

    function navSuccessFn(data, status, headers, config) {
      vm.facilities = vm.facilities.concat(data);   
      vm.facilities.next = data.next;
      Meta.setLoading(true);
    }

    function navErrorFn(data, status, headers, config) {
      console.log('That place does not exist or does not have facilities.');
    } 

    function searchSuccessFn(data, status, headers, config) {
      vm.facilities = data;
      vm.offset = 0;       
      Meta.setTitle("Afy360 | Search");
      Meta.setLoading(true);    
    }

    function searchErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('No results found, try again.');
    } 
  }
})();