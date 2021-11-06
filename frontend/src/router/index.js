import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path(.*)',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/auth-redirect',
    component: () => import('@/views/login/auth-redirect'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/error-page/404'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/error-page/401'),
    hidden: true
  },
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/dashboard/index'),
        name: 'Dashboard',
        meta: { title: '首页', icon: 'dashboard', affix: true }
      }
    ]
  },

  {
    path: '/profile',
    component: Layout,
    redirect: '/profile/index',
    hidden: true,
    children: [
      {
        path: 'index',
        component: () => import('@/views/profile/index'),
        name: 'Profile',
        meta: { title: '个人中心', icon: 'user', noCache: true }
      }
    ]
  },
  {
    path: '/dict/data/',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/dict/data/:id?',
        component: () => import('@/views/system/dict/data'),
        name: 'DictData',
        meta: { title: '字典数据明细', icon: 'dict', noCache: false }
      }
    ]
  },
  {
    path: '/proj',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/proj/:projectId',
        component: () => import('@/views/project/task_list'),
        name: '项目查看',
        meta: { title: '项目查看', }
      }
    ]
  },
  {
    path: '/task_detail',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/task_detail/:taskId',
        component: () => import('@/views/spider/currency/task_detail'),
        name: '任务详情',
        meta: { title: '任务详情', }
      }
    ]
  },

  {
    path: '/task_deploy',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/task_deploy/:taskId',
        component: () => import('@/views/spider/currency/task_deploy'),
        name: '任务部署',
        meta: { title: '任务部署', }
      }
    ]
  },

  // 主机
  {
    path: '/host_detail',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/host_detail/:uuid',
        component: () => import('@/views/host/host_detail'),
        name: '主机详情',
        meta: { title: '主机详情', }
      }
    ]
  },

  {
    path: '/host_deploy',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/host_deploy/:uuid',
        component: () => import('@/views/host/host_deploy'),
        name: '部署服务',
        meta: { title: '部署服务', }
      }
    ]
  },

  // 单机脚本日志

  {
    path: '/task_log',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/task_log/:taskId',
        component: () => import('@/views/spider/customized/log/task_log'),
        name: '任务日志',
        meta: { title: '任务日志', }
      }
    ]
  },


]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  // 404 page must be placed at the end !!!
  {
    path: '*',
    redirect: '/404',
    hidden: true
  }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
