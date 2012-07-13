# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
  },
  'target_defaults': {
    'conditions': [
      ['OS!="win"', {
        'defines': [
          # For talloc
          'HAVE_VA_COPY',
        ],
      }],
      ['OS!="mac"', {
        'defines': [
          # For talloc
          'HAVE_STRNLEN',
        ],
      }],
      ['os_posix == 1 and OS != "mac" and OS != "android"', {
        'cflags': [
          '-fPIC',
        ],
      }],
    ],
    'defines': [
      # For Mesa
      'MAPI_GLAPI_CURRENT',
    ],
  },
  'targets': [
    {
      'target_name': 'mesa',
      'type': 'static_library',
      'include_dirs': [
        '../talloc',
        'MesaLib/include',
        'MesaLib/src/glsl',
        'MesaLib/src/mapi',
        'MesaLib/src/mesa',
        'MesaLib/src/mesa/main',
      ],
      'sources': [
        '../talloc/talloc.c',
        'MesaLib/src/glsl/ast.h',
        'MesaLib/src/glsl/ast_expr.cpp',
        'MesaLib/src/glsl/ast_function.cpp',
        'MesaLib/src/glsl/ast_to_hir.cpp',
        'MesaLib/src/glsl/ast_type.cpp',
        'MesaLib/src/glsl/builtin_function.cpp',
        'MesaLib/src/glsl/builtin_types.h',
        'MesaLib/src/glsl/builtin_variables.h',
        'MesaLib/src/glsl/glsl_lexer.cpp',
        'MesaLib/src/glsl/glsl_parser.cpp',
        'MesaLib/src/glsl/glsl_parser.h',
        'MesaLib/src/glsl/glsl_parser_extras.cpp',
        'MesaLib/src/glsl/glsl_parser_extras.h',
        'MesaLib/src/glsl/glsl_symbol_table.cpp',
        'MesaLib/src/glsl/glsl_symbol_table.h',
        'MesaLib/src/glsl/glsl_types.cpp',
        'MesaLib/src/glsl/glsl_types.h',
        'MesaLib/src/glsl/hir_field_selection.cpp',
        'MesaLib/src/glsl/ir.cpp',
        'MesaLib/src/glsl/ir.h',
        'MesaLib/src/glsl/ir_algebraic.cpp',
        'MesaLib/src/glsl/ir_basic_block.cpp',
        'MesaLib/src/glsl/ir_basic_block.h',
        'MesaLib/src/glsl/ir_clone.cpp',
        'MesaLib/src/glsl/ir_constant_expression.cpp',
        'MesaLib/src/glsl/ir_constant_folding.cpp',
        'MesaLib/src/glsl/ir_constant_propagation.cpp',
        'MesaLib/src/glsl/ir_constant_variable.cpp',
        'MesaLib/src/glsl/ir_copy_propagation.cpp',
        'MesaLib/src/glsl/ir_dead_code.cpp',
        'MesaLib/src/glsl/ir_dead_code_local.cpp',
        'MesaLib/src/glsl/ir_dead_functions.cpp',
        'MesaLib/src/glsl/ir_div_to_mul_rcp.cpp',
        'MesaLib/src/glsl/ir_explog_to_explog2.cpp',
        'MesaLib/src/glsl/ir_expression_flattening.cpp',
        'MesaLib/src/glsl/ir_expression_flattening.h',
        'MesaLib/src/glsl/ir_function.cpp',
        'MesaLib/src/glsl/ir_function_can_inline.cpp',
        'MesaLib/src/glsl/ir_function_inlining.cpp',
        'MesaLib/src/glsl/ir_function_inlining.h',
        'MesaLib/src/glsl/ir_hierarchical_visitor.cpp',
        'MesaLib/src/glsl/ir_hierarchical_visitor.h',
        'MesaLib/src/glsl/ir_hv_accept.cpp',
        'MesaLib/src/glsl/ir_if_simplification.cpp',
        'MesaLib/src/glsl/ir_if_to_cond_assign.cpp',
        'MesaLib/src/glsl/ir_import_prototypes.cpp',
        'MesaLib/src/glsl/ir_lower_jumps.cpp',
        'MesaLib/src/glsl/ir_mat_op_to_vec.cpp',
        'MesaLib/src/glsl/ir_mod_to_fract.cpp',
        'MesaLib/src/glsl/ir_noop_swizzle.cpp',
        'MesaLib/src/glsl/ir_optimization.h',
        'MesaLib/src/glsl/ir_print_visitor.cpp',
        'MesaLib/src/glsl/ir_print_visitor.h',
        'MesaLib/src/glsl/ir_reader.cpp',
        'MesaLib/src/glsl/ir_reader.h',
        'MesaLib/src/glsl/ir_rvalue_visitor.cpp',
        'MesaLib/src/glsl/ir_rvalue_visitor.h',
        'MesaLib/src/glsl/ir_set_program_inouts.cpp',
        'MesaLib/src/glsl/ir_structure_splitting.cpp',
        'MesaLib/src/glsl/ir_sub_to_add_neg.cpp',
        'MesaLib/src/glsl/ir_swizzle_swizzle.cpp',
        'MesaLib/src/glsl/ir_tree_grafting.cpp',
        'MesaLib/src/glsl/ir_validate.cpp',
        'MesaLib/src/glsl/ir_variable.cpp',
        'MesaLib/src/glsl/ir_variable_refcount.cpp',
        'MesaLib/src/glsl/ir_variable_refcount.h',
        'MesaLib/src/glsl/ir_vec_index_to_cond_assign.cpp',
        'MesaLib/src/glsl/ir_vec_index_to_swizzle.cpp',
        'MesaLib/src/glsl/ir_visitor.h',
        'MesaLib/src/glsl/link_functions.cpp',
        'MesaLib/src/glsl/linker.cpp',
        'MesaLib/src/glsl/linker.h',
        'MesaLib/src/glsl/list.h',
        'MesaLib/src/glsl/loop_analysis.cpp',
        'MesaLib/src/glsl/loop_analysis.h',
        'MesaLib/src/glsl/loop_controls.cpp',
        'MesaLib/src/glsl/loop_unroll.cpp',
        'MesaLib/src/glsl/lower_noise.cpp',
        'MesaLib/src/glsl/lower_variable_index_to_cond_assign.cpp',
        'MesaLib/src/glsl/opt_redundant_jumps.cpp',
        'MesaLib/src/glsl/program.h',
        'MesaLib/src/glsl/s_expression.cpp',
        'MesaLib/src/glsl/s_expression.h',
        'MesaLib/src/glsl/safe_strcmp.c',
        'MesaLib/src/glsl/safe_strcmp.h',
        'MesaLib/src/glsl/glcpp/glcpp-lex.c',
        'MesaLib/src/glsl/glcpp/glcpp-parse.c',
        'MesaLib/src/glsl/glcpp/glcpp-parse.h',
        'MesaLib/src/glsl/glcpp/pp.c',
        'MesaLib/src/mapi/glapi/glapi.h',
        'MesaLib/src/mapi/glapi/glapi_dispatch.c',
        'MesaLib/src/mapi/glapi/glapi_entrypoint.c',
        'MesaLib/src/mapi/glapi/glapi_getproc.c',
        'MesaLib/src/mapi/glapi/glapi_nop.c',
        'MesaLib/src/mapi/glapi/glapi_priv.h',
        'MesaLib/src/mapi/glapi/glapidispatch.h',
        'MesaLib/src/mapi/glapi/glapioffsets.h',
        'MesaLib/src/mapi/glapi/glapitable.h',
        'MesaLib/src/mapi/glapi/glapitemp.h',
        'MesaLib/src/mapi/glapi/glprocs.h',
        'MesaLib/src/mapi/mapi/u_compiler.h',
        'MesaLib/src/mapi/mapi/u_current.c',
        'MesaLib/src/mapi/mapi/u_current.h',
        'MesaLib/src/mapi/mapi/u_execmem.c',
        'MesaLib/src/mapi/mapi/u_execmem.h',
        'MesaLib/src/mapi/mapi/u_macros.h',
        'MesaLib/src/mapi/mapi/u_thread.c',
        'MesaLib/src/mapi/mapi/u_thread.h',
        'MesaLib/src/mesa/main/accum.c',
        'MesaLib/src/mesa/main/accum.h',
        'MesaLib/src/mesa/main/api_arrayelt.c',
        'MesaLib/src/mesa/main/api_arrayelt.h',
        'MesaLib/src/mesa/main/api_exec.c',
        'MesaLib/src/mesa/main/api_exec.h',
        'MesaLib/src/mesa/main/api_loopback.c',
        'MesaLib/src/mesa/main/api_loopback.h',
        'MesaLib/src/mesa/main/api_noop.c',
        'MesaLib/src/mesa/main/api_noop.h',
        'MesaLib/src/mesa/main/api_validate.c',
        'MesaLib/src/mesa/main/api_validate.h',
        'MesaLib/src/mesa/main/arbprogram.c',
        'MesaLib/src/mesa/main/arbprogram.h',
        'MesaLib/src/mesa/main/arrayobj.c',
        'MesaLib/src/mesa/main/arrayobj.h',
        'MesaLib/src/mesa/main/atifragshader.c',
        'MesaLib/src/mesa/main/atifragshader.h',
        'MesaLib/src/mesa/main/attrib.c',
        'MesaLib/src/mesa/main/attrib.h',
        'MesaLib/src/mesa/main/bitset.h',
        'MesaLib/src/mesa/main/blend.c',
        'MesaLib/src/mesa/main/blend.h',
        'MesaLib/src/mesa/main/bufferobj.c',
        'MesaLib/src/mesa/main/bufferobj.h',
        'MesaLib/src/mesa/main/buffers.c',
        'MesaLib/src/mesa/main/buffers.h',
        'MesaLib/src/mesa/main/clear.c',
        'MesaLib/src/mesa/main/clear.h',
        'MesaLib/src/mesa/main/clip.c',
        'MesaLib/src/mesa/main/clip.h',
        'MesaLib/src/mesa/main/colormac.h',
        'MesaLib/src/mesa/main/colortab.c',
        'MesaLib/src/mesa/main/colortab.h',
        'MesaLib/src/mesa/main/compiler.h',
        'MesaLib/src/mesa/main/condrender.c',
        'MesaLib/src/mesa/main/condrender.h',
        'MesaLib/src/mesa/main/config.h',
        'MesaLib/src/mesa/main/context.c',
        'MesaLib/src/mesa/main/context.h',
        'MesaLib/src/mesa/main/convolve.c',
        'MesaLib/src/mesa/main/convolve.h',
        'MesaLib/src/mesa/main/core.h',
        'MesaLib/src/mesa/main/cpuinfo.c',
        'MesaLib/src/mesa/main/cpuinfo.h',
        'MesaLib/src/mesa/main/dd.h',
        'MesaLib/src/mesa/main/debug.c',
        'MesaLib/src/mesa/main/debug.h',
        'MesaLib/src/mesa/main/depth.c',
        'MesaLib/src/mesa/main/depth.h',
        'MesaLib/src/mesa/main/depthstencil.c',
        'MesaLib/src/mesa/main/depthstencil.h',
        'MesaLib/src/mesa/main/dispatch.h',
        'MesaLib/src/mesa/main/dlist.c',
        'MesaLib/src/mesa/main/dlist.h',
        'MesaLib/src/mesa/main/dlopen.c',
        'MesaLib/src/mesa/main/dlopen.h',
        'MesaLib/src/mesa/main/drawpix.c',
        'MesaLib/src/mesa/main/drawpix.h',
        'MesaLib/src/mesa/main/drawtex.c',
        'MesaLib/src/mesa/main/drawtex.h',
        'MesaLib/src/mesa/main/enable.c',
        'MesaLib/src/mesa/main/enable.h',
        'MesaLib/src/mesa/main/enums.c',
        'MesaLib/src/mesa/main/enums.h',
        'MesaLib/src/mesa/main/eval.c',
        'MesaLib/src/mesa/main/eval.h',
        'MesaLib/src/mesa/main/execmem.c',
        'MesaLib/src/mesa/main/extensions.c',
        'MesaLib/src/mesa/main/extensions.h',
        'MesaLib/src/mesa/main/fbobject.c',
        'MesaLib/src/mesa/main/fbobject.h',
        'MesaLib/src/mesa/main/feedback.c',
        'MesaLib/src/mesa/main/feedback.h',
        'MesaLib/src/mesa/main/ffvertex_prog.c',
        'MesaLib/src/mesa/main/ffvertex_prog.h',
        'MesaLib/src/mesa/main/fog.c',
        'MesaLib/src/mesa/main/fog.h',
        'MesaLib/src/mesa/main/formats.c',
        'MesaLib/src/mesa/main/formats.h',
        'MesaLib/src/mesa/main/framebuffer.c',
        'MesaLib/src/mesa/main/framebuffer.h',
        'MesaLib/src/mesa/main/get.c',
        'MesaLib/src/mesa/main/get.h',
        'MesaLib/src/mesa/main/getstring.c',
        'MesaLib/src/mesa/main/glheader.h',
        'MesaLib/src/mesa/main/hash.c',
        'MesaLib/src/mesa/main/hash.h',
        'MesaLib/src/mesa/main/hint.c',
        'MesaLib/src/mesa/main/hint.h',
        'MesaLib/src/mesa/main/histogram.c',
        'MesaLib/src/mesa/main/histogram.h',
        'MesaLib/src/mesa/main/image.c',
        'MesaLib/src/mesa/main/image.h',
        'MesaLib/src/mesa/main/imports.c',
        'MesaLib/src/mesa/main/imports.h',
        'MesaLib/src/mesa/main/light.c',
        'MesaLib/src/mesa/main/light.h',
        'MesaLib/src/mesa/main/lines.c',
        'MesaLib/src/mesa/main/lines.h',
        'MesaLib/src/mesa/main/macros.h',
        'MesaLib/src/mesa/main/matrix.c',
        'MesaLib/src/mesa/main/matrix.h',
        'MesaLib/src/mesa/main/mfeatures.h',
        'MesaLib/src/mesa/main/mipmap.c',
        'MesaLib/src/mesa/main/mipmap.h',
        'MesaLib/src/mesa/main/mm.c',
        'MesaLib/src/mesa/main/mm.h',
        'MesaLib/src/mesa/main/mtypes.h',
        'MesaLib/src/mesa/main/multisample.c',
        'MesaLib/src/mesa/main/multisample.h',
        'MesaLib/src/mesa/main/nvprogram.c',
        'MesaLib/src/mesa/main/nvprogram.h',
        'MesaLib/src/mesa/main/pixel.c',
        'MesaLib/src/mesa/main/pixel.h',
        'MesaLib/src/mesa/main/pixelstore.c',
        'MesaLib/src/mesa/main/pixelstore.h',
        'MesaLib/src/mesa/main/points.c',
        'MesaLib/src/mesa/main/points.h',
        'MesaLib/src/mesa/main/polygon.c',
        'MesaLib/src/mesa/main/polygon.h',
        'MesaLib/src/mesa/main/queryobj.c',
        'MesaLib/src/mesa/main/queryobj.h',
        'MesaLib/src/mesa/main/rastpos.c',
        'MesaLib/src/mesa/main/rastpos.h',
        'MesaLib/src/mesa/main/readpix.c',
        'MesaLib/src/mesa/main/readpix.h',
        'MesaLib/src/mesa/main/remap.c',
        'MesaLib/src/mesa/main/remap.h',
        'MesaLib/src/mesa/main/remap_helper.h',
        'MesaLib/src/mesa/main/renderbuffer.c',
        'MesaLib/src/mesa/main/renderbuffer.h',
        'MesaLib/src/mesa/main/scissor.c',
        'MesaLib/src/mesa/main/scissor.h',
        'MesaLib/src/mesa/main/shaderapi.c',
        'MesaLib/src/mesa/main/shaderapi.h',
        'MesaLib/src/mesa/main/shaderobj.c',
        'MesaLib/src/mesa/main/shaderobj.h',
        'MesaLib/src/mesa/main/shared.c',
        'MesaLib/src/mesa/main/shared.h',
        'MesaLib/src/mesa/main/simple_list.h',
        'MesaLib/src/mesa/main/state.c',
        'MesaLib/src/mesa/main/state.h',
        'MesaLib/src/mesa/main/stencil.c',
        'MesaLib/src/mesa/main/stencil.h',
        'MesaLib/src/mesa/main/syncobj.c',
        'MesaLib/src/mesa/main/syncobj.h',
        'MesaLib/src/mesa/main/texcompress.c',
        'MesaLib/src/mesa/main/texcompress.h',
        'MesaLib/src/mesa/main/texcompress_fxt1.c',
        'MesaLib/src/mesa/main/texcompress_fxt1.h',
        'MesaLib/src/mesa/main/texcompress_s3tc.c',
        'MesaLib/src/mesa/main/texcompress_s3tc.h',
        'MesaLib/src/mesa/main/texenv.c',
        'MesaLib/src/mesa/main/texenv.h',
        'MesaLib/src/mesa/main/texenvprogram.c',
        'MesaLib/src/mesa/main/texenvprogram.h',
        'MesaLib/src/mesa/main/texfetch.c',
        'MesaLib/src/mesa/main/texfetch.h',
        'MesaLib/src/mesa/main/texfetch_tmp.h',
        'MesaLib/src/mesa/main/texformat.c',
        'MesaLib/src/mesa/main/texformat.h',
        'MesaLib/src/mesa/main/texgen.c',
        'MesaLib/src/mesa/main/texgen.h',
        'MesaLib/src/mesa/main/texgetimage.c',
        'MesaLib/src/mesa/main/texgetimage.h',
        'MesaLib/src/mesa/main/teximage.c',
        'MesaLib/src/mesa/main/teximage.h',
        'MesaLib/src/mesa/main/texobj.c',
        'MesaLib/src/mesa/main/texobj.h',
        'MesaLib/src/mesa/main/texpal.c',
        'MesaLib/src/mesa/main/texpal.h',
        'MesaLib/src/mesa/main/texparam.c',
        'MesaLib/src/mesa/main/texparam.h',
        'MesaLib/src/mesa/main/texrender.c',
        'MesaLib/src/mesa/main/texrender.h',
        'MesaLib/src/mesa/main/texstate.c',
        'MesaLib/src/mesa/main/texstate.h',
        'MesaLib/src/mesa/main/texstore.c',
        'MesaLib/src/mesa/main/texstore.h',
        'MesaLib/src/mesa/main/transformfeedback.c',
        'MesaLib/src/mesa/main/transformfeedback.h',
        'MesaLib/src/mesa/main/uniforms.c',
        'MesaLib/src/mesa/main/uniforms.h',
        'MesaLib/src/mesa/main/varray.c',
        'MesaLib/src/mesa/main/varray.h',
        'MesaLib/src/mesa/main/version.c',
        'MesaLib/src/mesa/main/version.h',
        'MesaLib/src/mesa/main/viewport.c',
        'MesaLib/src/mesa/main/viewport.h',
        'MesaLib/src/mesa/main/vtxfmt.c',
        'MesaLib/src/mesa/main/vtxfmt.h',
        'MesaLib/src/mesa/main/vtxfmt_tmp.h',
        'MesaLib/src/mesa/math/m_clip_tmp.h',
        'MesaLib/src/mesa/math/m_copy_tmp.h',
        'MesaLib/src/mesa/math/m_debug.h',
        'MesaLib/src/mesa/math/m_debug_clip.c',
        'MesaLib/src/mesa/math/m_debug_norm.c',
        'MesaLib/src/mesa/math/m_debug_util.h',
        'MesaLib/src/mesa/math/m_debug_xform.c',
        'MesaLib/src/mesa/math/m_dotprod_tmp.h',
        'MesaLib/src/mesa/math/m_eval.c',
        'MesaLib/src/mesa/math/m_eval.h',
        'MesaLib/src/mesa/math/m_matrix.c',
        'MesaLib/src/mesa/math/m_matrix.h',
        'MesaLib/src/mesa/math/m_norm_tmp.h',
        'MesaLib/src/mesa/math/m_trans_tmp.h',
        'MesaLib/src/mesa/math/m_translate.c',
        'MesaLib/src/mesa/math/m_translate.h',
        'MesaLib/src/mesa/math/m_vector.c',
        'MesaLib/src/mesa/math/m_vector.h',
        'MesaLib/src/mesa/math/m_xform.c',
        'MesaLib/src/mesa/math/m_xform.h',
        'MesaLib/src/mesa/math/m_xform_tmp.h',
        'MesaLib/src/mesa/program/arbprogparse.c',
        'MesaLib/src/mesa/program/arbprogparse.h',
        'MesaLib/src/mesa/program/hash_table.c',
        'MesaLib/src/mesa/program/hash_table.h',
        'MesaLib/src/mesa/program/ir_to_mesa.cpp',
        'MesaLib/src/mesa/program/ir_to_mesa.h',
        'MesaLib/src/mesa/program/lex.yy.c',
        'MesaLib/src/mesa/program/nvfragparse.c',
        'MesaLib/src/mesa/program/nvfragparse.h',
        'MesaLib/src/mesa/program/nvvertparse.c',
        'MesaLib/src/mesa/program/nvvertparse.h',
        'MesaLib/src/mesa/program/prog_cache.c',
        'MesaLib/src/mesa/program/prog_cache.h',
        'MesaLib/src/mesa/program/prog_execute.c',
        'MesaLib/src/mesa/program/prog_execute.h',
        'MesaLib/src/mesa/program/prog_instruction.c',
        'MesaLib/src/mesa/program/prog_instruction.h',
        'MesaLib/src/mesa/program/prog_noise.c',
        'MesaLib/src/mesa/program/prog_noise.h',
        'MesaLib/src/mesa/program/prog_optimize.c',
        'MesaLib/src/mesa/program/prog_optimize.h',
        'MesaLib/src/mesa/program/prog_parameter.c',
        'MesaLib/src/mesa/program/prog_parameter.h',
        'MesaLib/src/mesa/program/prog_parameter_layout.c',
        'MesaLib/src/mesa/program/prog_parameter_layout.h',
        'MesaLib/src/mesa/program/prog_print.c',
        'MesaLib/src/mesa/program/prog_print.h',
        'MesaLib/src/mesa/program/prog_statevars.c',
        'MesaLib/src/mesa/program/prog_statevars.h',
        'MesaLib/src/mesa/program/prog_uniform.c',
        'MesaLib/src/mesa/program/prog_uniform.h',
        'MesaLib/src/mesa/program/program.c',
        'MesaLib/src/mesa/program/program.h',
        'MesaLib/src/mesa/program/program_parse.tab.c',
        'MesaLib/src/mesa/program/program_parse.tab.h',
        'MesaLib/src/mesa/program/program_parse_extra.c',
        'MesaLib/src/mesa/program/program_parser.h',
        'MesaLib/src/mesa/program/programopt.c',
        'MesaLib/src/mesa/program/programopt.h',
        'MesaLib/src/mesa/program/symbol_table.c',
        'MesaLib/src/mesa/program/symbol_table.h',
        'MesaLib/src/mesa/swrast/s_aaline.c',
        'MesaLib/src/mesa/swrast/s_aaline.h',
        'MesaLib/src/mesa/swrast/s_aalinetemp.h',
        'MesaLib/src/mesa/swrast/s_aatriangle.c',
        'MesaLib/src/mesa/swrast/s_aatriangle.h',
        'MesaLib/src/mesa/swrast/s_aatritemp.h',
        'MesaLib/src/mesa/swrast/s_accum.c',
        'MesaLib/src/mesa/swrast/s_accum.h',
        'MesaLib/src/mesa/swrast/s_alpha.c',
        'MesaLib/src/mesa/swrast/s_alpha.h',
        'MesaLib/src/mesa/swrast/s_atifragshader.c',
        'MesaLib/src/mesa/swrast/s_atifragshader.h',
        'MesaLib/src/mesa/swrast/s_bitmap.c',
        'MesaLib/src/mesa/swrast/s_blend.c',
        'MesaLib/src/mesa/swrast/s_blend.h',
        'MesaLib/src/mesa/swrast/s_blit.c',
        'MesaLib/src/mesa/swrast/s_clear.c',
        'MesaLib/src/mesa/swrast/s_context.c',
        'MesaLib/src/mesa/swrast/s_context.h',
        'MesaLib/src/mesa/swrast/s_copypix.c',
        'MesaLib/src/mesa/swrast/s_depth.c',
        'MesaLib/src/mesa/swrast/s_depth.h',
        'MesaLib/src/mesa/swrast/s_drawpix.c',
        'MesaLib/src/mesa/swrast/s_feedback.c',
        'MesaLib/src/mesa/swrast/s_feedback.h',
        'MesaLib/src/mesa/swrast/s_fog.c',
        'MesaLib/src/mesa/swrast/s_fog.h',
        'MesaLib/src/mesa/swrast/s_fragprog.c',
        'MesaLib/src/mesa/swrast/s_fragprog.h',
        'MesaLib/src/mesa/swrast/s_lines.c',
        'MesaLib/src/mesa/swrast/s_lines.h',
        'MesaLib/src/mesa/swrast/s_linetemp.h',
        'MesaLib/src/mesa/swrast/s_logic.c',
        'MesaLib/src/mesa/swrast/s_logic.h',
        'MesaLib/src/mesa/swrast/s_masking.c',
        'MesaLib/src/mesa/swrast/s_masking.h',
        'MesaLib/src/mesa/swrast/s_points.c',
        'MesaLib/src/mesa/swrast/s_points.h',
        'MesaLib/src/mesa/swrast/s_readpix.c',
        'MesaLib/src/mesa/swrast/s_span.c',
        'MesaLib/src/mesa/swrast/s_span.h',
        'MesaLib/src/mesa/swrast/s_spantemp.h',
        'MesaLib/src/mesa/swrast/s_stencil.c',
        'MesaLib/src/mesa/swrast/s_stencil.h',
        'MesaLib/src/mesa/swrast/s_texcombine.c',
        'MesaLib/src/mesa/swrast/s_texcombine.h',
        'MesaLib/src/mesa/swrast/s_texfilter.c',
        'MesaLib/src/mesa/swrast/s_texfilter.h',
        'MesaLib/src/mesa/swrast/s_triangle.c',
        'MesaLib/src/mesa/swrast/s_triangle.h',
        'MesaLib/src/mesa/swrast/s_trispan.h',
        'MesaLib/src/mesa/swrast/s_tritemp.h',
        'MesaLib/src/mesa/swrast/s_zoom.c',
        'MesaLib/src/mesa/swrast/s_zoom.h',
        'MesaLib/src/mesa/swrast/swrast.h',
        'MesaLib/src/mesa/swrast_setup/ss_context.c',
        'MesaLib/src/mesa/swrast_setup/ss_context.h',
        'MesaLib/src/mesa/swrast_setup/ss_triangle.c',
        'MesaLib/src/mesa/swrast_setup/ss_triangle.h',
        'MesaLib/src/mesa/swrast_setup/ss_tritmp.h',
        'MesaLib/src/mesa/swrast_setup/ss_vb.h',
        'MesaLib/src/mesa/swrast_setup/swrast_setup.h',
        'MesaLib/src/mesa/tnl/t_context.c',
        'MesaLib/src/mesa/tnl/t_context.h',
        'MesaLib/src/mesa/tnl/t_draw.c',
        'MesaLib/src/mesa/tnl/t_pipeline.c',
        'MesaLib/src/mesa/tnl/t_pipeline.h',
        'MesaLib/src/mesa/tnl/t_rasterpos.c',
        'MesaLib/src/mesa/tnl/t_vb_cliptmp.h',
        'MesaLib/src/mesa/tnl/t_vb_cull.c',
        'MesaLib/src/mesa/tnl/t_vb_fog.c',
        'MesaLib/src/mesa/tnl/t_vb_light.c',
        'MesaLib/src/mesa/tnl/t_vb_lighttmp.h',
        'MesaLib/src/mesa/tnl/t_vb_normals.c',
        'MesaLib/src/mesa/tnl/t_vb_points.c',
        'MesaLib/src/mesa/tnl/t_vb_program.c',
        'MesaLib/src/mesa/tnl/t_vb_render.c',
        'MesaLib/src/mesa/tnl/t_vb_rendertmp.h',
        'MesaLib/src/mesa/tnl/t_vb_texgen.c',
        'MesaLib/src/mesa/tnl/t_vb_texmat.c',
        'MesaLib/src/mesa/tnl/t_vb_vertex.c',
        'MesaLib/src/mesa/tnl/t_vertex.c',
        'MesaLib/src/mesa/tnl/t_vertex.h',
        'MesaLib/src/mesa/tnl/t_vertex_generic.c',
        'MesaLib/src/mesa/tnl/t_vertex_sse.c',
        'MesaLib/src/mesa/tnl/t_vp_build.c',
        'MesaLib/src/mesa/tnl/t_vp_build.h',
        'MesaLib/src/mesa/tnl/tnl.h',
        'MesaLib/src/mesa/vbo/vbo.h',
        'MesaLib/src/mesa/vbo/vbo_attrib.h',
        'MesaLib/src/mesa/vbo/vbo_attrib_tmp.h',
        'MesaLib/src/mesa/vbo/vbo_context.c',
        'MesaLib/src/mesa/vbo/vbo_context.h',
        'MesaLib/src/mesa/vbo/vbo_exec.c',
        'MesaLib/src/mesa/vbo/vbo_exec.h',
        'MesaLib/src/mesa/vbo/vbo_exec_api.c',
        'MesaLib/src/mesa/vbo/vbo_exec_array.c',
        'MesaLib/src/mesa/vbo/vbo_exec_draw.c',
        'MesaLib/src/mesa/vbo/vbo_exec_eval.c',
        'MesaLib/src/mesa/vbo/vbo_rebase.c',
        'MesaLib/src/mesa/vbo/vbo_save.c',
        'MesaLib/src/mesa/vbo/vbo_save.h',
        'MesaLib/src/mesa/vbo/vbo_save_api.c',
        'MesaLib/src/mesa/vbo/vbo_save_draw.c',
        'MesaLib/src/mesa/vbo/vbo_save_loopback.c',
        'MesaLib/src/mesa/vbo/vbo_split.c',
        'MesaLib/src/mesa/vbo/vbo_split.h',
        'MesaLib/src/mesa/vbo/vbo_split_copy.c',
        'MesaLib/src/mesa/vbo/vbo_split_inplace.c',
      ],
      'conditions': [
        ['clang == 1', {
          'xcode_settings': {
            'WARNING_CFLAGS': [
              # Several functions ignore the result of talloc_steal().
              '-Wno-unused-value',
              # texenvprogram.c converts '~0' to a bitfield, which causes clang
              # to warn that -1 is implicitly converted to 255.
              '-Wno-constant-conversion',
              # https://bugs.freedesktop.org/show_bug.cgi?id=51574
              '-Wno-self-assign-memvar',
            ],
          },
          'cflags': [
            '-Wno-unused-value',
            '-Wno-constant-conversion',
            '-Wno-self-assign-memvar',
          ],
        }],
      ],
    },
    # Building this target will hide the native OpenGL shared library and
    # replace it with a slow software renderer.
    {
      'target_name': 'osmesa',
      'type': 'loadable_module',
      'mac_bundle': 0,
      'dependencies': [
        'mesa',
      ],
      # Fixes link problems on Mac OS X with missing __cxa_pure_virtual.
      'conditions': [
        ['OS=="mac"', {
          'sources': [
            'MesaLib/src/mesa/drivers/osmesa/empty.cpp',
          ],
        }],
      ],
      'include_dirs': [
        'MesaLib/include',
        'MesaLib/src/mapi',
        'MesaLib/src/mesa',
        'MesaLib/src/mesa/drivers',
      ],
      'sources': [
        'MesaLib/src/mesa/drivers/common/driverfuncs.c',
        'MesaLib/src/mesa/drivers/common/driverfuncs.h',
        'MesaLib/src/mesa/drivers/common/meta.c',
        'MesaLib/src/mesa/drivers/common/meta.h',
        'MesaLib/src/mesa/drivers/osmesa/osmesa.c',
        'MesaLib/src/mesa/drivers/osmesa/osmesa.def',
      ],
    },
  ],
}
