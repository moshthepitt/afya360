/**
* HomeController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('HomeController', HomeController)

  HomeController.$inject = ['$scope', 'Restangular', 'Meta'];

  /**
  * @namespace HomeController
  */
  function HomeController($scope, Restangular, Meta) {
    var vm = this; 
    vm.next = next;
    vm.back = back;   

    Restangular.setDefaultRequestParams('get', {limit: 20, format: 'json'});

    activate();

    function activate() {
      vm.facilities = Restangular.all('health-facilities/').getList({offset:0}).$object;
      vm.offset = 0;
      Meta.setTitle("Afy360 | Buzz");
    }  

    function next() {
      vm.offset += 20;
      vm.facilities = Restangular.all('health-facilities/').getList({offset:vm.offset}).$object;  
    } 

    function back() {
      vm.offset = vm.offset - 20;
      vm.facilities = Restangular.all('health-facilities/').getList({offset:vm.offset}).$object;
    }   
  }
})();