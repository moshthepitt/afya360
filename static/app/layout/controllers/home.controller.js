/**
* HomeController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('HomeController', HomeController)

  HomeController.$inject = ['$scope', '$location', 'Restangular', 'Meta'];

  /**
  * @namespace HomeController
  */
  function HomeController($scope, $location, Restangular, Meta) {
    var vm = this; 
    vm.next = next;
    vm.back = back;   

    Restangular.setDefaultRequestParams('get', {limit: 20, format: 'json'});

    activate();

    function activate() {
      Restangular.all('health-facilities/').getList({offset:0}).then(homeSuccessFn, homeErrorFn);
    }  

    function next() {
      vm.offset += 20;
      vm.facilities = Restangular.all('health-facilities/').getList({offset:vm.offset}).$object;  
    } 

    function back() {
      vm.offset = vm.offset - 20;
      vm.facilities = Restangular.all('health-facilities/').getList({offset:vm.offset}).$object;
    }   

    function homeSuccessFn(data, status, headers, config) {
      vm.facilities = data;
      vm.offset = 0;
      Meta.setTitle("Afy360 | Kenya Directory of Health Centers");    
    }

    function homeErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('Error.');
    } 
  }
})();