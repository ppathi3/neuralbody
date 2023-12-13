# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# compile CUDA with /usr/local/cuda/bin/nvcc
CUDA_DEFINES = -DPYTORCH_VERSION=20001 -DTV_CUDA

CUDA_INCLUDES = --options-file CMakeFiles/spconv_nms.dir/includes_CUDA.rsp

CUDA_FLAGS = "--expt-relaxed-constexpr" -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -DONNX_NAMESPACE=onnx_c2 -gencode arch=compute_75,code=sm_75 -Xcudafe --diag_suppress=cc_clobber_ignored,--diag_suppress=integer_sign_change,--diag_suppress=useless_using_declaration,--diag_suppress=set_but_not_used,--diag_suppress=field_without_dll_interface,--diag_suppress=base_class_has_different_dll_interface,--diag_suppress=dll_interface_conflict_none_assumed,--diag_suppress=dll_interface_conflict_dllexport_assumed,--diag_suppress=implicit_return_from_non_void_function,--diag_suppress=unsigned_compare_with_zero,--diag_suppress=declared_but_not_referenced,--diag_suppress=bad_friend_decl --expt-relaxed-constexpr --expt-extended-lambda -gencode arch=compute_75,code=sm_75 -O3 -DNDEBUG -std=c++14 -Xcompiler=-fPIC

