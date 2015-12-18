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
    vm.back = back; 
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
      // vm.facilities = Restangular.all('hf-search/').getList(request_params).$object;  
      // Restangular.all('hf-search/').getList(request_params).then(function(resultThreads){
      //   console.log(resultThreads);
      //   // vm.facilities.push(resultThreads);
      // });

      Restangular.all('hf-search/').getList(request_params).then(xsearchSuccessFn, searchErrorFn);

    } 

    function xsearchSuccessFn(data, status, headers, config) {
      console.log(data);
      // vm.facilities.push(data);
    }

    function back() {
      vm.offset = vm.offset - 20;
      request_params['offset'] = vm.offset;
      vm.facilities = Restangular.all('hf-search/').getList(request_params).$object;
    }  

    function submit() {
      if (vm.q === undefined || vm.q == null) {
        // do nothing
      }  else {
        $location.url('/search').search({q: vm.q});
      }
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