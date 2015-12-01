/**
* SearchController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('SearchController', SearchController)

  SearchController.$inject = ['$scope', '$routeParams', 'Restangular', 'Meta'];

  /**
  * @namespace SearchController
  */
  function SearchController($scope, $routeParams, Restangular, Meta) {
    var vm = this; 
    vm.next = next;
    vm.back = back; 

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
      vm.facilities = Restangular.all('hf-search/').getList(request_params).$object;  
    } 

    function back() {
      vm.offset = vm.offset - 20;
      request_params['offset'] = vm.offset;
      vm.facilities = Restangular.all('hf-search/').getList(request_params).$object;
    }  

    function searchSuccessFn(data, status, headers, config) {
      vm.facilities = data;
      vm.offset = 0;
      Meta.setTitle("Afy360 | Search");     
    }

    function searchErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('No results found, try again.');
    } 
  }
})();