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
    vm.submit = submit;

    Meta.setLoading(false);
    Meta.setTitle("Afya360 | Kenya Directory of Health Facilities"); 
    activate();

    function activate() {
      Restangular.one('home-resources').get().then(homeSuccessFn, homeErrorFn);
    }  

    function submit() {
      if (vm.q === undefined || vm.q == null) {
        // do nothing
      }  else {
        $location.url('/search').search({q: vm.q});
      }
    } 

    function homeSuccessFn(data, status, headers, config) {
      vm.facilities = data.facilities;
      vm.counties = data.counties;
      vm.constituencies = data.constituencies;      
      Meta.setLoading(true);
      Meta.setTitle("Afya360 | Kenya Directory of Health Facilities"); 
    }

    function homeErrorFn(data, status, headers, config) {
      $location.url('/');
      console.log('Error.');
    } 
  }
})();