/**
* FacilitiesController
* @namespace afya360.facilities.controllers
*/
(function () {
  'use strict';

  angular
    .module('afya360.facilities.controllers')
    .controller('FacilitiesController', FacilitiesController);

  FacilitiesController.$inject = ['$scope'];

  /**
  * @namespace FacilitiesController
  */
  function FacilitiesController($scope) {
    var vm = this;

    activate();


    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf afya360.facilities.controllers.FacilitiesController
    */
    function activate() {
      $scope.$watchCollection(function () { return $scope.facilities; }, render);
    }

    /**
    * @name render
    * @desc Renders Posts into columns of approximately equal height
    * @param {Array} current The current value of `vm.facilities`
    * @param {Array} original The value of `vm.facilities` before it was updated
    * @memberOf afya360.facilities.controllers.FacilitiesController
    */
    function render(current, original) {
      if (current !== original) {        
          for (var i = 0; i < current.length; ++i) {
          original.push(current[i]);
        }
      } 
    }

  }
})();