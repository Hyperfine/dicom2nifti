import os
import dicom2nifti

# example data for demo purpose
DATA_DIR = '/data/tmp/lyao/data/dicom_to_nifti_quick_start'

YALE_LOWFIELD_DICOMS = os.path.join(DATA_DIR, 'yale_lowfield/DICOMDIR')
YALE_LOWFIELD_NIFTIS = os.path.join(DATA_DIR, 'yale_lowfield/NIFTIS')

YALE_HIGHFIELD_DICOMS = os.path.join(DATA_DIR, 'yale_highfield/DICOMDIR')
YALE_HIGHFIELD_NIFTIS = os.path.join(DATA_DIR, 'yale_highfield/NIFTIS')

HOPPR_HIGHFIELD_DICOMS = os.path.join(DATA_DIR, 'hoppr_highfield/DICOMDIR')
HOPPR_HIGHFIELD_NIFTIS = os.path.join(DATA_DIR, 'hoppr_highfield/NIFTIS')


def main(mode):
    if mode == 'yale_lowfield':
        os.makedirs(YALE_LOWFIELD_NIFTIS, exist_ok=True)
        cmd = f'dcm2niix -ba n -f pid@%i@@series@%s@@desp@%d -o {YALE_LOWFIELD_NIFTIS} {YALE_LOWFIELD_DICOMS}'
        os.system(cmd)
    elif mode == 'yale_highfield':
        dicom2nifti.settings.validate_orthogonal = False
        dicom2nifti.settings.validate_slicecount = True
        dicom2nifti.settings.validate_orientation = True
        os.makedirs(YALE_HIGHFIELD_NIFTIS, exist_ok = True)
        dicom2nifti.convert_dir.convert_directory(
            YALE_HIGHFIELD_DICOMS, YALE_HIGHFIELD_NIFTIS, compression=False)
    elif mode == 'hoppr_highfield':
        dicom2nifti.settings.validate_slice_increment = True
        os.makedirs(HOPPR_HIGHFIELD_NIFTIS, exist_ok=True)
        dicom2nifti.convert_dir.convert_directory(
            HOPPR_HIGHFIELD_DICOMS, HOPPR_HIGHFIELD_NIFTIS, compression=False)
    else:
        raise NotImplementedError()


if __name__ == '__main__':
    #main('yale_lowfield')
    #main('yale_highfield')
    main('hoppr_highfield')
