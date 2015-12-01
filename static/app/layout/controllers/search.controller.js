/**
* SearchController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('SearchController', SearchController)

  SearchController.$inject = ['$scope', 'Restangular', 'Meta'];

  /**
  * @namespace SearchController
  */
  function SearchController($scope, Restangular, Meta) {
    var vm = this; 
    vm.next = next;
    vm.back = back;   

    Restangular.setDefaultRequestParams('get', {limit: 20, format: 'json'});

    activate();

    function activate() {
      Restangular.all('hf-search/').getList({offset:0, text:'abc'}).then(searchSuccessFn, searchErrorFn);      
    }  

    function next() {
      vm.offset += 20;
      vm.facilities = Restangular.all('hf-search/').getList({offset:vm.offset}).$object;  
    } 

    function back() {
      vm.offset = vm.offset - 20;
      vm.facilities = Restangular.all('hf-search/').getList({offset:vm.offset}).$object;
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