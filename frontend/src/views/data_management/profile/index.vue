<template>
  <div class="app-container">
    <el-row :gutter="20">

      <!--用户数据-->
      <el-col :span="20" :xs="24">
        <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px">
          <el-form-item label="用户编号" prop="username">
            <el-input
              v-model="queryParams.username"
              placeholder="请输入用户编号"
              clearable
              size="small"
              style="width: 240px"
              @keyup.enter.native="handleQuery"
            />
          </el-form-item>
          <el-form-item label="用户名称" prop="nickname">
            <el-input
              v-model="queryParams.nickname"
              placeholder="请输入用户名称"
              clearable
              size="small"
              style="width: 240px"
              @keyup.enter.native="handleQuery"
            />
          </el-form-item>
          <el-form-item label="状态" prop="status">
            <el-select v-model="queryParams.status" placeholder="用户状态" clearable size="small" style="width: 240px">
              <el-option v-for="dict in statusOptions" :key="dict.id" :label="dict.label" :value="dict.label" />
            </el-select>
          </el-form-item>

          <!-- <el-form-item>
            <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
            <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
          </el-form-item> -->
        </el-form>

        <!-- <el-row :gutter="10" class="mb8">
          <el-col :span="1.5">
            <el-button type="primary" icon="el-icon-plus" size="mini" @click="handleAdd">新增</el-button>
          </el-col>
          <el-col :span="1.5">
            <el-button type="success" icon="el-icon-edit" size="mini" :disabled="single" @click="handleUpdate">修改
            </el-button>
          </el-col>
          <el-col :span="1.5">
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              :disabled="multiple"
              @click="handleDelete"
            >删除
            </el-button>
          </el-col>
          <el-col :span="1.5">
            <el-button
              type="info"
              icon="el-icon-upload2"
              size="mini"
              @click="handleImport"
            >导入
            </el-button>
          </el-col>
          <el-col :span="1.5">
            <el-button
              type="warning"
              icon="el-icon-download"
              size="mini"
              @click="handleExport"
            >导出
            </el-button>
          </el-col>
        </el-row> -->

        <el-table v-loading="loading" :data="userList">
          <el-table-column type="selection" width="50" align="center" />
          <el-table-column label="讲解点id" align="center" prop="讲解点id" :show-overflow-tooltip="true" />
          <el-table-column label="博物馆名称" align="center" prop="博物馆名称" :show-overflow-tooltip="true" />
          <el-table-column label="所属国家" align="center" prop="所属国家" :show-overflow-tooltip="true" />
          <el-table-column label="所属国家id" align="center" prop="所属国家id" width="120" />
          <el-table-column label="所属城市" align="center" prop="所属城市" :show-overflow-tooltip="true" />

        </el-table>
        <pagination
          v-show="total>0"
          :total="total"
          @pagination="getList"
        />
      </el-col>
    </el-row>

  </div>
</template>

<script>
import {
  get_data_list
} from '@/api/xhs'
import { getToken } from '@/utils/auth'
import Treeselect from '@riophae/vue-treeselect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'

export default {
  name: 'User',
  components: { Treeselect },
  data() {
    return {
      // 遮罩层
      loading: true,
      // 选中数组
      ids: [],
      // 非单个禁用
      single: true,
      // 非多个禁用
      multiple: true,
      // 总条数
      total: 0,
      // 用户表格数据
      userList: null,
      // 弹出层标题
      title: '',
      // 部门树选项
      deptOptions: undefined,
      // 是否显示弹出层
      open: false,
      // 部门名称
      deptName: undefined,
      // 状态数据字典
      statusOptions: [],
      // 性别状态字典
      sexOptions: [],
      // 岗位选项
      postOptions: [],
      // 角色选项
      roleOptions: [],
      // 表单参数
      form: {},
      defaultProps: {
        children: 'children',
        label: 'name'
      },
      // 用户导入参数
      upload: {
        // 是否显示弹出层（用户导入）
        open: false,
        // 弹出层标题（用户导入）
        title: '',
        // 是否禁用上传
        isUploading: false,
        // 是否更新已经存在的用户数据
        updateSupport: 0,
        // 设置上传的请求头部
        headers: { Authorization: 'Bearer ' + getToken() },
        // 上传的地址
        url: process.env.VUE_APP_BASE_API + '/system/user/importData'
      },
      // 查询参数
      queryParams: {
        page: 1,
        limit: 10,
        username: undefined,
        nickname: undefined,
        status: undefined,
        deptId: undefined
      },
      // 表单校验
      rules: {
        username: [
          { required: true, message: '用户编号不能为空', trigger: 'blur' }
        ],
        nickname: [
          { required: true, message: '用户名称不能为空', trigger: 'blur' }
        ],
        deptId: [
          { required: true, message: '归属部门不能为空', trigger: 'blur' }
        ],
        identity_card: [
          { required: true, message: '身份证不能为空', trigger: 'blur' }
        ],
        phone: [
          { required: true, message: '手机号码不能为空', trigger: 'blur' },
          {
            pattern: /^1[3|4|5|6|7|8|9][0-9]\d{8}$/,
            message: '请输入正确的手机号码',
            trigger: 'blur'
          }
        ],
        sex: [
          { required: true, message: '性别不能为空', trigger: 'blur' }
        ],
        status: [
          { required: true, message: '状态不能为空', trigger: 'blur' }
        ]
      },
      excel_name: 'system_user'
    }
  },

  created() {
    this.getList()
  },

  methods: {
    /** 查询用户列表 */
    getList() {
      this.loading = true
      get_data_list().then(response => {
        this.userList = response.data.items
        this.loading = false
      }
      )
    }

  }
}
</script>
