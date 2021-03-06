
import Cookies from 'js-cookie'

import 'normalize.css/normalize.css' // a modern alternative to CSS resets
import Element from 'element-ui'
import './styles/element-variables.scss'

// import enLang from 'element-ui/lib/locale/lang/en'// 如果使用中文语言包请默认支持，无需额外引入，请删除该依赖

import '@/styles/index.scss' // global css
import '@/styles/ruoyi.scss' // ruoyi css

// 全局引入
import AudioPlayer from '@liripeng/vue-audio-player'
import '@liripeng/vue-audio-player/lib/vue-audio-player.css'

Vue.use(AudioPlayer)

import ElImageViewer from "element-ui/packages/image/src/image-viewer";

Vue.use(ElImageViewer)

import './icons' // icon
import './permission' // permission control
import './utils/error-log' // error log
import { getDicts } from '@/api/system/dict/data'
import { resetForm, selectDictLabel, download, handleTree } from '@/utils/ruoyi'
import Pagination from '@/components/Pagination'
import * as filters from './filters' // global filters


import Vue from 'vue'
import App from './App'
import store from './store'
import router from './router'


// 全局方法挂载
import dayjs from "dayjs"

Vue.prototype.dayjs = dayjs;//可以全局使用dayjs

Vue.prototype.getDicts = getDicts
Vue.prototype.resetForm = resetForm
Vue.prototype.selectDictLabel = selectDictLabel
Vue.prototype.download = download
Vue.prototype.handleTree = handleTree

Vue.prototype.msgSuccess = function (msg) {
  this.$message({ showClose: true, message: msg, type: 'success' })
}

Vue.prototype.msgError = function (msg) {
  this.$message({ showClose: true, message: msg, type: 'error' })
}

Vue.prototype.msgInfo = function (msg) {
  this.$message.info(msg)
}

// 全局组件挂载
Vue.component('Pagination', Pagination)
Vue.component('ElImageViewer', ElImageViewer)

// 按钮级别权限配置
// import button_permission from './directive/button_permission'
// Vue.use(button_permission)

Vue.use(Element, {
  size: Cookies.get('size') || 'smail', // set element-ui default size
  // locale: enLang // 如果使用中文，无需设置，请删除
})

// register global utility filters
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
