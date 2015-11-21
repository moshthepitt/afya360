/**
* IndexController
* @namespace afya360.layout.controllers
*/
(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Facilities', 'djResource'];

  /**
  * @namespace IndexController
  */
  function IndexController($scope, Facilities, djResource) {
    var vm = this;

    var Animal = djResource('api/v1/provinces/:id/', {'id': "@id"});
    vm.facilities = Animal.query({limit:2});
    // vm.facilities = [];

    // activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf afya360.layout.controllers.IndexController
    */
    function activate() {      
      vm.facilities = Facilities.all(); //.then(facilitiesSuccessFn, facilitiesErrorFn);

      /**
      * @name facilitiesSuccessFn
      * @desc Update facilities array on view
      */
      function facilitiesSuccessFn(data, status, headers, config) {
        vm.facilities = data.data;
      }


      /**
      * @name facilitiesErrorFn
      * @desc Show snackbar with error
      */
      function facilitiesErrorFn(data, status, headers, config) {
        console.log(data.error);
      }
    }
  }
})();